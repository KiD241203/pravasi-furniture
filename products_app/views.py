from django.shortcuts import render
from . models import Category , products

# Create your views here.

def products(request):
    return render(request,'products/products.html')

def product_detailes(request):
    return render(request, 'products/products_detailes.html')

def category_products(request  ):
    
    return render(request,'products/category_products.html')