from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request, 'shop.html')

def product_detail(request):
    return render(request, 'product_detail.html')