from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.orders, name='orders'),
    path('order_details/<int:id>',views.order_details, name='order_details'),
    
    # admin urls
    
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('manage_orders/',views.manage_orders,name='manage_orders'),
    path('update_order_status/<int:id>',views.update_order_status,name='update_order_status'),
    
]
