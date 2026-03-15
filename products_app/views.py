from django.shortcuts import render ,get_object_or_404
from . models import Category , products

# Create your views here.

def product(request):
    
    productt = products.objects.all()
    context = {
        'productt':productt
    }
    
    
    return render(request,'products/products.html',context)

def product_detailes(request,id):
    product = products.objects.get(id=id)
        
    return render(request, 'products/products_detailes.html',{'product':product})

def category_products(request,id):
    category = Category.objects.get(id=id)
    product = products.objects.filter(category=category)
    
    context = {
        'category':category,
        'products':product
    }
    return render(request,'products/category_products.html',context)