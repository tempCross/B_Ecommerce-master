from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"
    
def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)

def checkout(request):
    return render(request, "checkout-page.html")

def products(request):
    return render(request, "product-page.html")