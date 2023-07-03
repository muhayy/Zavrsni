from django.shortcuts import render

def home(request):
    return render(request, "index.html", locals())

def account(request):
    return render(request, "account.html", locals())

def cart(request):
    return render(request, "cart.html", locals())

def product_details(request):
    return render(request, "frankincense-essential-oil.html", locals())

def products(request):
    return render(request, "products.html", locals())

def product_details2(request):
    return render(request, "lemon-essential-oil.html", locals())

def product_details3(request):
    return render(request, "ricinusovo-ulje.html", locals())

def product_details4(request):
    return render(request, "ulje-sjemenki-grozda.html", locals())

def product_details5(request):
    return render(request, "setovi-difuzora-aroma-trske.html", locals())

def product_details6(request):
    return render(request, "himalajska-ruzicasta-sol-za-kupku.html", locals())

def product_details7(request):
    return render(request, "herbal-glo-vitamin-c-losion.html", locals())

def product_details8(request):
    return render(request, "ulje-jojobe.html", locals())

def product_details9(request):
    return render(request, "avokado-ulje.html", locals())

def product_details10(request):
    return render(request, "masazno-ulje-kamelije.html", locals())

def product_details11(request):
    return render(request, "kokosovo-ulje.html", locals())

def product_details12(request):
    return render(request, "etericno-ulje-bosiljka.html", locals())

def coupons(request):
    return render(request, "coupons.html", locals())

def vaucer_details(request):
    return render(request, "poklon-vaucer-masaza-facial.html", locals())

def vaucer_details2(request):
    return render(request, "poklon-vaucer-masaza.html", locals())

def vaucer_details3(request):
    return render(request, "poklon-vaucer-masaza-facial-fullbodystretch.html", locals())

def about(request):
    return render(request, "onama.html", locals())

def register(request):
    return render(request, "registration/register.html", locals())


