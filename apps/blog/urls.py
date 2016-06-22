from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.authtoken import views as drf_views

from . import views
from .api import views as api_views

router = routers.DefaultRouter()
# router.register(r'user', api_views.UserViewSet)

app_name = 'blog'

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    # url(r'^api-token-auth/', drf_views.obtain_auth_token),
    url(r'^api/v1/user/auth/$', api_views.ObtainAuthToken.as_view()),
    url(r'^api/v1/user/reg/$', api_views.RegisterUserView.as_view()),
    url(r'^api/v1/user/$', api_views.UserProfile.as_view()),
    url(r'^api/v1/user/posts/$', api_views.UserPosts.as_view()),
    url(r'^api/v1/post/$', api_views.PostList.as_view()),
    url(r'^api/v1/post/search/(?P<query>.+)$', api_views.PostSearch.as_view()),
    url(r'^api/v1/post/search/$', api_views.PostSearch.as_view()),

    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
