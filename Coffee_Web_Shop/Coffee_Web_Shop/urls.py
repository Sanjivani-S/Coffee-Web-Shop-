"""
URL configuration for Coffee_Web_Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_Coffee_Web_Shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shop, name="shop"),
    path('user_login/',views.user_login, name = 'user_login'),
    path ('user_logout/', views.user_logout, name = "user_logout"),
    path('register/', views.register, name="register"),
    path('error/', views.error, name="error"),
    path('product_detail/<int:id>/', views.product_detail, name="product_detail"),
    path('cart_summary/', views.cart_summary, name="cart_summary"),
    path('add/', views.cart_add, name="cart_add"),
    path('delete/', views.cart_delete, name="cart_delete"),
    path('update/', views.cart_update, name="cart_update"),


]
