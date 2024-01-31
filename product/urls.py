
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.myproduct),
    path('list',views.productlist,name='product_list'),
    path('<int:proid>',views.productdetailes,name="product.detailes"),

]
