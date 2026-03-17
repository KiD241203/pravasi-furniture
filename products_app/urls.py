from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.product, name='products'),
    path('product_dtl/<int:id>/',views.product_detailes, name='product_detailes'),
    path('category_products/<int:id>/',views.category_products, name='category_products'),
    
    # admin urls
    
    path('add_product/',views.add_product,name='add_product'),
    path('manage_products/',views.manage_products,name='manage_products'),
    
]
