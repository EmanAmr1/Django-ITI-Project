
from django.urls import path,include
from . import views
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
   
    path('',views.myproduct),
    path('list',views.productlist,name='product_list'),
    path('<int:proid>',views.productdetailes,name="product.detailes"),
    path('new',views.addpro,name="product.add"),
    path('delete/<int:proid>',views.deletepro,name="product.delete"),
    path('update/<int:proid>',views.updatepro,name="product.update"),
    path('newForm',views.addFormpro,name="product.addForm"),
    path('newMetaForm', views.addMetaFormPro, name="product.addMetaForm"),
    path('mygenericUpdate<pk>',login_required(ProductGenericUpdate.as_view()),name="product.GenericUpdat"),
    path('mygenericProDetailes<pk>',login_required(ProductGenericDetails.as_view()),name="product.GenericDetails"),
    path('mygenericProDelete<pk>',login_required(ProductGenericDelete.as_view()),name="product.GenericDelete"),
    path('mygenericProList',login_required(ProductGenericlist.as_view()),name="product.GenericList"),
    path('mygenericProCreate', login_required(ProductGenericCreate.as_view()),name="product.GenericCreate"),
    path("API/",include("product.api.urls")),
]
