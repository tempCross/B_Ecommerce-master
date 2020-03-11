from django.urls import path
from . import views
from .views import (
    CheckoutView, 
    products,
    HomeView,
    ItemDetailView,
    add_to_cart,
    OrderSummaryView,
    remove_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    FilterShirtView,
    FilterSportwearView,
    remove_single_item_from_cart,
    process_payment,
    payment_done,
    payment_cancelled
)
app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product-page'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/',RequestRefundView.as_view(), name='request-refund' ),
    path('process-payment/', process_payment, name='process-payment'),
    path('payment-done/', payment_done, name='payment-done'),
    path('payment-cancelled/', payment_cancelled, name='payment-cancelled'),
    path('filter-shirt-view/', FilterShirtView.as_view(), name='filter-shirt-view'),
    path('filter-sportwear-view/', FilterSportwearView.as_view(), name='filter-sportwear-view')
]