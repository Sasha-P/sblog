from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DUser, Group as DGroup
from django.contrib.sessions.models import Session
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from rest_framework import viewsets

from apps.studdb.api.serializers import UserSerializer, GroupSerializer, SessionSerializer
from .forms import LoginForm, RegistrationForm, GroupForm, StudentForm
from .models import Group, Student


class LoginView(generic.View):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
            else:
                # Return a 'disabled account' error message
                message = "Your username and password didn't match. Please try again."
        else:
            # Return an 'invalid login' error message.
            message = "Please provide username and password."
        return render(request, self.template_name, {'form': form, 'message': message})


class RegisterView(generic.FormView):
    form_class = RegistrationForm
    success_url = "/"
    template_name = "registration/registration.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterView, self).form_valid(form)


class IndexView(generic.View):
    # template_name = 'studdb/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'studdb/index.html')


@method_decorator(login_required, name='dispatch')
class GroupListView(generic.ListView):
    model = Group
    template_name = 'studdb/groups_list.html'
    context_object_name = 'groups'


@method_decorator(login_required, name='dispatch')
class GroupDetailView(generic.DetailView):
    model = Group
    template_name = 'studdb/group_detail.html'
    context_object_name = 'group'


@method_decorator(login_required, name='dispatch')
class GroupCreateView(generic.CreateView):
    model = Group
    form_class = GroupForm

    def get_context_data(self, **kwargs):
        context = super(GroupCreateView, self).get_context_data(**kwargs)
        context['is_new'] = True
        return context


@method_decorator(login_required, name='dispatch')
class GroupUpdateView(generic.UpdateView):
    model = Group
    form_class = GroupForm

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['is_new'] = False
        return context


@method_decorator(login_required, name='dispatch')
class GroupDeleteView(generic.DeleteView):
    model = Group
    success_url = reverse_lazy('studdb:groups_list')


@method_decorator(login_required, name='dispatch')
class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['is_new'] = True
        return context


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['is_new'] = False
        return context


@method_decorator(login_required, name='dispatch')
class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('studdb:group_detail')
