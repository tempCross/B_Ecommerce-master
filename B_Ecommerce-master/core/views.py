from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from .models import Item, OrderItem, Order
from django.utils import timezone
# Create your views here.

class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home-page.html"
    
def checkout(request):
    return render(request, "checkout-page.html")

def products(request):
    return render(request, "product-page.html")

class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect("core:product-page", slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("core:product-page", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect("core:product-page", slug=slug)
    
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart")
            return redirect("core:product-page", slug=slug)
        else:
            # add a message saying the user doesn't have an order
            messages.info(request, "This item was not in your cart")
            return redirect("core:product-page", slug=slug)
    else:
        # add a message saying the user doesnt have an order
        messages.info(request, "You do not have an active order")
        return redirect("core:product-page", slug=slug)
