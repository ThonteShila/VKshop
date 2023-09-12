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
                product_details=Product_details.objects.all()
                print(product_details)
                print(product_details)
                context={
                        'product_details':product_details,
                }
                return render(request,"index.html",context) 
def aboutus(request):
        return render(request,'aboutus.html',{})
def contactus(request):
        return render(request,'contactus.html',{})
def products(request):
        print(request.POST)
        if request.method=="POST":                
                if 'add_product' in request.POST:
                        return redirect("../add_product")                
                return render(request,"products.html")
        else:   
                product_details=Product_details.objects.all()
                print(product_details)
                context={
                        'product_details':product_details,
                }
                return render(request,"products.html",context)    

def add_product(request, product_id):
        print(request.method)
        if request.method=="POST":
                productname=request.POST.get('product_name')
                slug=request.POST.get('slug')
                cat_name=request.POST.get('category_name')
                cat_slug=request.POST.get('category_slug')
                cat_img=request.POST.get('category_image')
                price=request.POST.get('price')
                pro_desc=request.POST.get('product_description')
                pro_image=request.POST.get('product_image')
                
                product_details=Product_details(product_name=productname,slug=slug,category_name=cat_name,category_slug=cat_slug,category_image=cat_img,price=price,product_description=pro_desc,product_image=pro_image)
                product_details.save()
                message="Product data saved successfully!"
                context={
                        'product_details':product_details,
                        'functionality_name':"Create New",
                        'message':message
                }
                return render(request,"add_product.html",context)
        elif request.method=="GET":
                print(" else GET")
                if product_id==0:
                        product_details=Product_details()
                        func_name="Create New" 
                else:
                        product_details=Product_details.objects.get(pk=product_id)  
                        func_name="Modify"  
                message=""
                context={            
                        'functionality_name':func_name,
                        'message':message,
                        'product_details':product_details,
                }
              
                print("add_listing else before render")
                return render(request,'add_product.html',context)
        else:
                print("add_listing outer else ")
                message=""
                context={
                        'functionality_name':"Create New",
                        'message':message,
                }   
                return render(request,"add_product.html",{})   

def delete_product(request,product_id):
        message=""
        if request.method=="GET":
                product_details=Product_details.objects.get(pk=product_id).delete()              
                print("in Get:", id)
                message="One Record Removed"
                print("in message:", message)
                return redirect("../products/")
        return render(request,"products.html",{'message':message})


