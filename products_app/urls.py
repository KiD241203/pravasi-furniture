from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.products, name='products'),
    path('product_dtl/',views.product_detailes, name='product_detailes'),
    path('category_products/',views.category_products, name='category_products')
    
]
