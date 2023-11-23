from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from app_Coffee_Web_Shop.registration_form import RegistrationForm


# Create your views here.

def shop(request):
    return render(request, 'shop.html')

def product_detail(request):
    return render(request, 'product_detail.html')

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