from django.contrib.auth.models import User as DUser, Group as DGroup
from django.contrib.sessions.models import Session
from django.utils import timezone
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer, SessionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # lookup_field = 'user-detail'


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DGroup.objects.all()
    serializer_class = GroupSerializer


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class ActiveUsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        # Query all non-expired sessions
        # use timezone.now() instead of datetime.now() in latest versions of Django
        sessions = Session.objects.filter(expire_date__gte=timezone.now())
        uid_list = []

        # Build a list of user ids from that query
        for session in sessions:
            data = session.get_decoded()
            uid_list.append(data.get('_auth_user_id', None))

        # Query all logged in users based on id list
        return DUser.objects.filter(id__in=uid_list)
