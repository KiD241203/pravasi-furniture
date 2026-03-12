from django.shortcuts import render
from products_app.models import Category , products

# Create your views here.

def index(request):
    category = Category.objects.all()
    product = products.objects.all() 
    context = {
        'category':category,
        'product':product
    }
    return render(request,'home/index.html',context)
