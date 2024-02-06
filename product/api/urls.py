from django.urls import path
from .views import *

urlpatterns = [
path('Hello/',Hello,name='Hello' ),
path('acceptdata/',acceptdata,name='acceptdata' ),
path('getAllProducts/',getAllProducts,name='getAllProducts' ),
path('getProduct/<int:proid>/',getProduct,name='getProduct' ),
path('addProduct/',addProduct,name='addProduct' ),
path('updateProduct/<int:proid>/',updateProduct,name='updateProduct' ),
path('deleteProduct/<int:proid>/',deleteProduct,name='deleteProduct' ),
path('GetAllProductsg/',GetAllProductsg.as_view(),name='GetAllProductsg' ),
path('GetAllProductsC/',GetAllProductsC.as_view(),name='GetAllProductsC' ),
]