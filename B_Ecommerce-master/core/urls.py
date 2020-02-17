from django.urls import path
from .views import (
    item_list, 
    checkout, 
    products,
    HomeView
)
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item-list'),
    path('checkout/', checkout, name='checkout'),
    path('products/', products, name='products')
]