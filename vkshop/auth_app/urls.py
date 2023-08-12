from django.contrib import admin
from django.urls import path,include
from auth_app import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    
]