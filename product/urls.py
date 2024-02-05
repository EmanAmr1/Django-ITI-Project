
from django.urls import path
from . import views
from .views import *
urlpatterns = [
   
    path('',views.myproduct),
    path('list',views.productlist,name='product_list'),
    path('<int:proid>',views.productdetailes,name="product.detailes"),
    path('new',views.addpro,name="product.add"),
    path('delete/<int:proid>',views.deletepro,name="product.delete"),
    path('update/<int:proid>',views.updatepro,name="product.update"),
    path('newForm',views.addFormpro,name="product.addForm"),
    path('newMetaForm', views.addMetaFormPro, name="product.addMetaForm"),
    path('mygenericUpdate<pk>', ProductGenericUpdate.as_view(),name="product.GenericUpdat"),
    path('mygenericProDetailes<pk>', ProductGenericDetails.as_view(),name="product.GenericDetails"),
    path('mygenericProDelete<pk>', ProductGenericDelete.as_view(),name="product.GenericDelete"),
    path('mygenericProList', ProductGenericlist.as_view(),name="product.GenericList"),
    path('mygenericProCreate', ProductGenericCreate.as_view(),name="product.GenericCreate"),
]
