from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'activeusers', views.ActiveUsersViewSet, 'activeusers')

app_name = 'studdb'
urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^groups/$', views.GroupListView.as_view(), name='groups_list'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetailView.as_view(), name='group_detail'),
    url(r'^group/new/$', views.GroupCreateView.as_view(), name='group_new'),
    url(r'^group/(?P<pk>\d+)/edit/$', views.GroupUpdateView.as_view(), name='group_edit'),
    url(r'^group/(?P<pk>\d+)/remove/$', views.GroupDeleteView.as_view(), name='group_remove'),
    url(r'^student/new/$', views.StudentCreateView.as_view(), name='student_new'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.StudentUpdateView.as_view(), name='student_edit'),
    url(r'^student/(?P<pk>\d+)/remove/$', views.StudentDeleteView.as_view(), name='student_remove'),
]