from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.mycategory),
    path('list',views.categorylist,name='category_list'),
    path('<int:catid>',views.categorydetailes,name='category.detailes'),

]