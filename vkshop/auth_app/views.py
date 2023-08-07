from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('conform_password')
        if pass1!=pass2:
            message="Password not matching"
            return HttpResponse("Password not matching")
        try:
            if User.objects.get(username=email):
                message="Email already exists"
                return HttpResponse("Email already exists")
        except  Exception as identifier:
            pass
        user=User.objects.create_user(email,email,pass1)
        message="user created"
        user.save()
        return HttpResponse("user created")

    return render(request,'authentication/signup.html',{})
def login(request):
    return render(request,'authentication/login.html',{})
def logout(request):
    return redirect('/auth_app/login')
# Create your views here.
