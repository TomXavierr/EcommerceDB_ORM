from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop,name='shop'),
    path('product_details',views.product_details,name= 'product_details'),
   
]