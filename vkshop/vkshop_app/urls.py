from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contactus/',views.contactus,name='contactus'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('products/',views.products,name='products'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    #path('edit_product/<int:product_id>',views.edit_product,name='edit_product'),
    path('delete_product/<int:product_id>',views.delete_product,name='delete_product'),
    path('add_product/<int:product_id>', views.add_product, name='add_product'), 
]
