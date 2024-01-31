from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.aboutlist,name="aboutus_list"),
  

]