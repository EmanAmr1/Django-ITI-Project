from django.urls import path
from . import views

urlpatterns = [

    path('', views.mycategory),
    path('list', views.categorylist, name='category_list'),
    path('<int:catid>', views.categorydetailes, name='category.detailes'),
    path('new', views.addcat, name="category.add"),
    path('delete/<int:catid>', views.deletecat, name="category.delete"),
    path('update/<int:catid>',views.updatecat,name="category.update"),
    path('newForm',views.addFormcat,name="category.addForm"),
]
