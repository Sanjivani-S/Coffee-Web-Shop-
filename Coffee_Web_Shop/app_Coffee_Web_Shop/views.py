from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from app_Coffee_Web_Shop.registration_form import RegistrationForm
from django.urls import reverse
import random
from .models import Product

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages

# Create your views here.

def shop(request):
    products = Product.objects.order_by('nr_available')
    display_products = []
    for p in products:
        display_products.append({'id': p.pk, 'name': p.name, 'img': "img/" + p.img.url, 'price': str(p.price).replace(".", ":")})
    return render(request, 'shop.html', {'products': display_products})

def user_login(request):
    msg = 'not_logged_in'

    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('shop'))
            else:
                return HttpResponse("Your account is not active")
        else:
            print("User with Username: {} and Password {} failed to login".format(username, password))
            msg = 'login_failed'
            return render (request, 'login.html', {'msg': msg} )
    else:
        return render (request, 'login.html' ,{'msg': msg})    

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('shop'))
  
def product_detail(request, id):
    #If a non-existing id is supplied, go to the error page instead
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        product = None
        return render(request, 'error.html')
    
    display_product = {'id': product.pk, 'name': product.name, 'img': "img/" + product.img.url, 'price': str(product.price).replace(".", ":"), 'description': product.description}

    #Other "similar products"
    products = Product.objects.order_by('nr_available')
    related_items = []
    for p in products:
        if p.pk != product.pk:
            related_items.append({'id': p.pk, 'name': p.name, 'img': "img/" + p.img.url, 'price': str(p.price).replace(".", ":")})

    random.shuffle(related_items)

    if len(related_items) > 4:
        related_items = related_items[:4]

    return render(request, 'product_detail.html', {'product': display_product, 'related_items': related_items})

def register(request):
    registered = False

    if request.method == 'POST':
        regform = RegistrationForm(request.POST)
        

        if regform.is_valid():
            user = regform.save()
            user.set_password(user.password)
            user.save()
            

            registered = True

        else:
            print(regform.errors)

    else:
        regform = RegistrationForm()

    return render(request,'registration.html',
                    {'regform':regform,
                     'registered':registered})

def error(request):
    return render(request, 'error.html')
