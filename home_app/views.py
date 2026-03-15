from django.shortcuts import render
from products_app.models import Category , products
from . models import HeroCategory

# Create your views here.

def index(request):
    category = Category.objects.all()
    product = products.objects.all()[:4] 
    heroCategory = HeroCategory.objects.all()
    context = {
        'category':category,
        'product':product,
        'heroCategory':heroCategory
    }
    return render(request,'home/index.html',context)
