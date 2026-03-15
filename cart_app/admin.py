from django.contrib import admin
from . models import Placed_Order,Order_Item
# Register your models here.

admin.site.register(Placed_Order)
admin.site.register(Order_Item)