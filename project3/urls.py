"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('register/',register,name='register'),
    path('New_user/',New_user,name='New_user'),
    path('login_user/',login_user,name='login_user'),
    path('logout_user/',logout_user,name='logout_user'),
    path('user_data/',user_data,name='user_data'),
]
