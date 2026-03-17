from django.shortcuts import render , get_object_or_404,redirect
from cart_app.models import Placed_Order,Order_Item
from products_app.models import products
from django.db.models import Sum
# Create your views here.

def orders(request):
    orders = Placed_Order.objects.all()
    order_item = Order_Item.objects.all()
    context ={
        'orders': orders,
        'order_item':order_item
    }
    return render(request, 'orders/Customer_orders.html', context )


def order_details(request,id):
    order = Placed_Order.objects.get(id=id)
    items = Order_Item.objects.filter(order=order)
    context ={
        'order':order,
        'items':items
    }
    return render(request, 'orders/Order_detail.html',context)


def admin_dashboard(request):
    total_orders = Placed_Order.objects.count()
    total_products = products.objects.count()
    pending_orders = Placed_Order.objects.filter(order_status='Placed').count()
    total_revanue = Placed_Order.objects.aggregate(total=Sum('total_price'))['total'] or 0
    recent_orders = Placed_Order.objects.order_by('-created_at')[:5]
    
    context = {
        
        'total_orders':total_orders,
        'total_products':total_products,
        'pending_orders':pending_orders,
        'total_revanue':total_revanue,
        'recent_orders':recent_orders
    }
    
    return render(request,'orders/Admin_dashboard.html',context)


def manage_orders(request):
    
    placed_orders = Placed_Order.objects.filter(order_status='Placed')
    Processing = Placed_Order.objects.filter(order_status='Processing')
    Shipped = Placed_Order.objects.filter(order_status='Shipped')
    Delivered = Placed_Order.objects.filter(order_status='Delivered')
    
    context ={
        'Placed_orders':placed_orders,
        'Processing_orders':Processing,
        'Shipped_orders':Shipped,
        'Delivered_orders':Delivered,
    }
    
    return render(request,'orders/manage_orders.html',context)

def update_order_status(request,id):
    if request.method == 'POST':
        order =  get_object_or_404(Placed_Order, id=id)
        new_status = request.POST.get('status')
        
        order.order_status = new_status
        order.save()
    return redirect('manage_orders')