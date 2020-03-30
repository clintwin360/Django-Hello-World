"""clintwin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# New additions.
from clintwinsponsor import views
from django.conf.urls import url
from django.urls import path, include 
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')), 
	path('accounts/logout/', auth_views.LogoutView.as_view(template_name= 'registration/logged_out.html'), name='LogOut'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('accounts/password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	
	path('', TemplateView.as_view(template_name='index.html'), name='index'),     
	path('about', views.AboutPageView.as_view(), name='about'),
    path('how_works', views.HowWorksPageView.as_view(), name='how_works'),
	path('contact', views.ContactPageView.as_view(), name='contact'),
	path('directions', views.DirectionsPageView.as_view(), name='directions'),
	path('create_trial_form', views.ClinicalTrialCreateView.as_view(), name='create_trial_form'),
	
]

