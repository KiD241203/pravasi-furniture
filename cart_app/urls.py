from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.cart , name='cart'),
    
    path('add_to_cart/<int:id>/',views.add_to_cart , name='add_to_cart'),
 
    path('remove/<int:id>/', views.remove_from_cart, name='remove'),

    path('increase/<int:id>/', views.increase_qty, name='increase'),

    path('decrease/<int:id>/', views.decrease_qty, name='decrease'),
    
    path('check_out', views.check_out, name='check_out'),
]
