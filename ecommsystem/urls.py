"""ecommsystem URL Configuration

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
from django.urls import path, include
from accounts import views as ac
#from modelForms import views as pc


urlpatterns = [
    path('admin/', admin.site.urls),
#    path('accounts/', include('accounts.urls')),
    path('register/', ac.register, name='register'),
    path('login/', ac.login_user, name='login_user'),
    path('logout/', ac.logout_user, name='logout_user'),
#    path('home/', ac.home, name='home'),
    path('accounts/home/', ac.home, name='home'),

    path('user_register/', ac.student_register.as_view(), name='student_register'),
    path('admin_register/', ac.teacher_register.as_view(), name='teacher_register'),
#    path('',pc.index),
#    path('listProjects/',pc.listProjects),
#    path('addProject/',pc.addProject)



]
