from django.shortcuts import render
from django.urls import reverse
import random

from .models import Product

# Create your views here.

def shop(request):
    products = Product.objects.order_by('nr_available')
    display_products = []
    for p in products:
        display_products.append({'id': p.pk, 'name': p.name, 'img': "img/" + p.img.url, 'price': str(p.price).replace(".", ":")})
    return render(request, 'shop.html', {'products': display_products})

def product_detail(request, id):
    #If a non-existing id is supplied, go to the error page instead
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        product = None
        return render(request, 'error.html')
    
    display_product = {'id': product.pk, 'name': product.name, 'img': "img/" + product.img.url, 'price': str(product.price).replace(".", ":")}

    #Other "similar products"
    products = Product.objects.order_by('nr_available')
    related_items = []
    for p in products:
        if p.pk != product.pk:
            related_items.append({'id': p.pk, 'name': p.name, 'img': "img/" + p.img.url, 'price': str(p.price).replace(".", ":")})

    random.shuffle(related_items)

    if len(related_items) > 4:
        related_items = related_items[:3]

    return render(request, 'product_detail.html', {'product': display_product, 'related_items': related_items})

def error(request):
    return render(request, 'error.html')