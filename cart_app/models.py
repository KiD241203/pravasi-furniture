from django.db import models

# Create your models here.

class Placed_Order(models.Model):
    name = models.CharField( max_length=100)
    phone = models.CharField( max_length=10)
    email = models.EmailField( max_length=254)
    
    address = models.TextField()
    pincode = models.CharField( max_length=10)
    city = models.CharField( max_length=150)
    
    payment_method = models.CharField( max_length=50)
    total_price = models.DecimalField( max_digits=10, decimal_places=2)
    created_at = models.DateTimeField ( auto_now_add=True)
    
    STATUS = (
        ('Placed','Order Placed'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered')
    )
    
    order_status = models.CharField( max_length=50, choices=STATUS,default='Placed')
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table = 'placed_order'
        

class Order_Item(models.Model):
    order = models.ForeignKey(Placed_Order, on_delete=models.CASCADE, related_name='order_items')
    product_name = models.CharField( max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField( max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product_name} (Order: {self.order.id})"
    
    class Meta:
        db_table = 'order_item'
        

