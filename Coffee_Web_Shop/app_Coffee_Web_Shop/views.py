from django.shortcuts import render

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages

# Create your views here.

def shop(request):
    return render(request, 'shop.html')

def product_detail(request):
    return render(request, 'product_detail.html')

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