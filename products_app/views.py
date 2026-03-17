from django.shortcuts import render ,get_object_or_404 , redirect
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



# admin ---

def add_product(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        image = request.FILES.get('image')  # ✅ FIXED
        price = request.POST.get('price')
        description = request.POST.get('description')
        category_id = request.POST.get('category')

        if not category_id:
            categories = Category.objects.all()
            return render(request,'products/admin_add_product.html',{
                'categories': categories,
                # 'error': 'Please select category'
            })

        category = get_object_or_404(Category, id=category_id)

        products.objects.create(
            name=name,
            image=image,
            price=price,
            category=category,
            description=description
        )

        return redirect('admin_dashboard')

    categories = Category.objects.all()

    return render(request,'products/admin_add_product.html',{
        'categories': categories
    })
    
    
def manage_products(request):
    All_products = products.objects.all()
    count = products.objects.count()
    
    
    context = {
        'all_products':All_products,
        'count':count
    }
    return render(request,'products/manage_products.html',context)