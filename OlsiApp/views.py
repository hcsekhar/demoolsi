from .models import *
from django.shortcuts import render

# Create your views here.
def home(req):
    products_data = product_DB.objects.all()
    return render(req, 'OlsiAppHTML/index.html', {'data':products_data})

def faq(req):
    return render(req, 'OlsiAppHTML/faq.html', {'title': 'OLSI | FAQ'})

def login(req):
    return render(req, 'OlsiAppHTML/login_reg.html')

def contact(req):
    return render(req, 'OlsiAppHTML/contact.html')

def galery(req):
    return render(req, 'OlsiAppHTML/galery.html')


def business(req):
    return render(req, 'OlsiAppHTML/business.html')

def underconstrunction(req):
    return render(req, 'OlsiAppHTML/404.html')

def aboutus(req):
    return render(req, 'OlsiAppHTML/Aboutus.html')

def agriculture(req):
    return render(req, 'OlsiAppHTML/agriculture.html')

def manufacture(req):
    return render(req, 'OlsiAppHTML/manufacture.html')



def products(req):
    products_data = product_DB.objects.all()
    return render(req,'OlsiAppHTML/products.html', {'data':products_data})

def viewproduct(req, id):
    viewproduct_data = product_DB.objects.get(pk=id)
    print(product_DB.pk, id)
    return render(req, 'OlsiAppHTML/viewproduct.html', {'i':viewproduct_data})
    
def userSignIn(req, id):
    pass


