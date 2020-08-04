from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    allProds = [[products, range(1,nSlides), nSlides], [products, range(1,nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def contact(request):
    return render(request, 'shop/contactus.html')

def about(request):
    return render(request, 'shop/about.html')

def tracker(request):
    return HttpResponse("We are in Shop Traacker")

def search(request):
    return HttpResponse("We are in Shop Search")

def productView(request):
    return HttpResponse("We are in Shop Product View")

def checkout(request):
    return HttpResponse("We are in Shop Checkout")
    
def careers(request):
    return HttpResponse("We are in Shop careers")

