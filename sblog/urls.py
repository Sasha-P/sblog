"""sblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views

from rest_framework import routers
from apps.studdb import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'activeusers', views.ActiveUsersViewSet, 'activeusers')

admin.autodiscover()

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/registration/$', views.RegisterView.as_view(), name='registration'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, kwargs={'next_page': '/'}, name='logout'),
    url(r'', include('apps.studdb.urls')),
    url(r'^blog/', include('apps.blog.urls')),
]
