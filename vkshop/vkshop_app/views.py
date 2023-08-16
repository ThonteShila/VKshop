from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib import messages
from django.utils.encoding import force_bytes,force_text
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Owner_details,Product_details
def signup(request):        
        return render(request,"authentication/signup.html",{})       
def login(request):
        return render(request,'authentication/login.html',{})
def logout(request):
        return redirect('/')
def index(request):
        return render(request,'index.html',{})
def aboutus(request):
        return render(request,'aboutus.html',{})
def contactus(request):
        return render(request,'contactus.html',{})

def add_product(request, product_id):
        print(request.method)
        if request.method=="POST":
                return render(request,"add_product.html",{})
        else:
                print("HHHHHHHHHHHH")
                return render(request,"add_product.html",{})
