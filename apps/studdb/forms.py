from django import forms
from .models import Group, Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    class Meta:
        fields = ('username', 'password', )


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.widgets.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    password2 = forms.CharField(
        label="Password confirmation",
        help_text="Enter the same password as before, for verification.",
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    first_name = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    last_name = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    patronymic = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    birthday = forms.DateField(
        help_text="Date format YYYY-MM-DD.",
        widget=forms.widgets.DateInput(attrs={'class': 'form-control'}),
        required=True
    )
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.widgets.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        patronymic = self.cleaned_data['patronymic']
        birthday = self.cleaned_data['birthday']
        group = self.cleaned_data['group']

        user.email = self.cleaned_data['email']
        user.first_name = first_name
        user.last_name = last_name
        user.set_password = self.cleaned_data['password1']

        student = Student(
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            birthday=birthday,
            group=group
        )

        if commit:
            user.save()
            student.save()

        return user


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'patronymic', 'birthday', 'group', )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name', 'monitor', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'monitor': forms.Select(attrs={'class': 'form-control'}),
        }
