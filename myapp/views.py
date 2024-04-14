

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def index(request):
    return render(request, 'index.html', {})


def order_digital_appliances(request):
    da_product = DigitalAppliances.objects.all()
    return render(request, 'order_digital_appliances.html',{'products':da_product})

def order_groceries(request):
    g_products = Groceries.objects.all()
    return render(request, 'order_groceries.html', {'products':g_products})

def order_clothes(request):
    c_products = Clothing.objects.all()
    return render(request, 'order_clothes.html', {'products': c_products})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete  = False)
        items = order.orderitem_set.all()
    else:
        items = []


    return render(request, 'cart.html',{'items':items, 'order': order})

from django.shortcuts import render

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete  = False)
        items = order.orderitem_set.all()
    else:
        order  = {'get_cart_items':0, 'get_cart_total':0}
        items = []
    return render(request, 'checkout.html', {'items': items, 'order': order})

@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action', action)
    print('productId', productId)
    
    # Fetch the product based on its type
    product = None
    if 'clothing_id' in data:
        product = Clothing.objects.get(id=productId)
    elif 'digital_appliance_id' in data:
        product = DigitalAppliances.objects.get(id=productId)
    elif 'groceries_id' in data:
        product = Groceries.objects.get(id=productId)

    if product is None:
        return JsonResponse({'error': 'Product not found'}, status=404)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added ', safe=False)