

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .models import Clothing

def index(request):
    return render(request, 'index.html', {})

def order_digital_appliances(request):
    return render(request, 'order_digital_appliances.html',{})

def order_groceries(request):
    return render(request, 'order_groceries.html', {})

def order_clothes(request):
    return render(request, 'order_clothes.html',{})

def wishlist(request):
    return render(request, 'wishlist.html',{})

def cart(request):
    return render(request, 'cart.html',{})

from django.shortcuts import render

def checkout(request):
    # Logic to retrieve items from the cart and calculate total price
    cart_items = []  # Placeholder for cart items
    total_price = 0  # Placeholder for total price calculation

    # If you have a form for shipping and payment details, handle form submission here
    if request.method == 'POST':
        # Process form data
        pass  # Placeholder for processing form data

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})
