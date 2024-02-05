
from django.urls import path,include
from .views import *

urlpatterns = [
   
    
    path('',include('django.contrib.auth.urls')),
    path('profile/',myprofile,name='myprofile'),
    path('register/',RegisterForm.as_view(),name='myregister'),
] 