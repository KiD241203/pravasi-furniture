from django.shortcuts import render, redirect, get_object_or_404
from products_app.models import products 
from . models import Placed_Order,Order_Item


def add_to_cart(request, id):

    product = get_object_or_404(products, id=id)

    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER'))

def cart(request):

    cart = request.session.get('cart', {})

    cart_products = []
    total = 0

    for key, value in cart.items():

        product = products.objects.get(id=key)

        product.quantity = value
        product.total_price = product.price * value

        total += product.total_price

        cart_products.append(product)

    context = {
        'products': cart_products,
        'total': total
    }

    return render(request, 'cart/cart.html', context)


def remove_from_cart(request, id):

    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart

    return redirect('cart')


def increase_qty(request, id):

    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1

    request.session['cart'] = cart

    return redirect('cart')


def decrease_qty(request, id):

    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] -= 1

        if cart[str(id)] <= 0:
            del cart[str(id)]

    request.session['cart'] = cart

    return redirect('cart')



# Checkout 

def check_out(request):
    cart = request.session.get('cart', {})
    cart_products = []
    total = 0
    
    for key, value in cart.items():

        product = products.objects.get(id=key)

        product.quantity = value
        product.total_price = product.price * value

        total += product.total_price

        cart_products.append(product)
    
    if request.method == 'POST':
       
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        payment_method = request.POST.get('payment_method')
        
        
        order = Placed_Order.objects.create(
            name=name,  
            phone=phone,
            email=email,
            address=address,
            pincode=pincode,
            city=city,
            payment_method=payment_method,
            total_price=total
        )
        
        for item in cart_products:
            Order_Item.objects.create(
                order=order,
                product_name=item.name,
                quantity=item.quantity,
                price=item.price
            )
            
        request.session['cart'] = {}
        return redirect('cart')
    
    context = {
        'products': cart_products,
        'total': total
    }
        
    
    return render(request,'cart/checkout.html', context )