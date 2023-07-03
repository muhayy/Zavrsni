"""ZavrsniProjekat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
import ZavrsniProjekat.view.myview as myview
from prijava import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', myview.home),
    path('cart', myview.cart),
    path('frankincense_essential_oil', myview.product_details),
    path('products', myview.products),
    path('', myview.home),
    path('lemon-essential-oil', myview.product_details2),
    path('ricinusovo-ulje', myview.product_details3),
    path('ulje-od-sjemenki-grozda', myview.product_details4),
    path('setovi-difuzora-aroma-trske', myview.product_details5),
    path('himalajska-ruzicasta-sol-za-kupku', myview.product_details6),
    path('herbal-glo-vitamin-c-losion', myview.product_details7),
    path('ulje-jojobe', myview.product_details8),
    path('avokado-ulje', myview.product_details9),
    path('masazno-ulje-kamelije', myview.product_details10),
    path('kokosovo-ulje', myview.product_details11),
    path('etericno-ulje-bosiljka', myview.product_details12),
    path('coupons', myview.coupons),
    path('poklon-vaucer-masaza-facial', myview.vaucer_details),
    path('poklon-vaucer-masaza', myview.vaucer_details2),
    path('poklon-vaucer-masaza-facial-fullbodystretch', myview.vaucer_details3),
    path('about', myview.about),
    path('register/', views.register),
    path('account/', views.user_login),
]
