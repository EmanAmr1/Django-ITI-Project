
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.myproduct),
    path('list',views.productlist,name='product_list'),
    path('<int:proid>',views.productdetailes,name="product.detailes"),
    path('new',views.addpro,name="product.add"),
    path('delete/<int:proid>',views.deletepro,name="product.delete"),
    path('update/<int:proid>',views.updatepro,name="product.update"),
    path('newForm',views.addFormpro,name="product.addForm"),
]
