from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib import messages
from .utils import generate_token,TokenGenerator
from django.utils.encoding import force_bytes,force_text
from django.core.mail import EmailMessage
from django.conf import settings
def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('conform_password')
        if pass1!=pass2:
            messages.warning(request,"Password is not matching")
            return render(request,"authentication/signup.html")
        try:
            if User.objects.get(username=email):
                messages.info(request,"Email already exists")
                return render(request,"authentication/signup.html")
        except  Exception as identifier:
            pass
        user=User.objects.create_user(email,email,pass1)
        user.is_active=False
        user.save()
        email_subject="activate your account"
        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127:0:0:1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })
        email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,['email'])
        email_message.send()
        messages.success(request,"Activate your account by clicking lin in your gmail")
        return redirect('/auth_app/login/')
        messages.warning(request,"User created Successfully")
        return render(request,"authentication/signup.html")
    return render(request,'authentication/signup.html',{})
def login(request):
    return render(request,'authentication/login.html',{})
def logout(request):
    return redirect('/auth_app/login')

