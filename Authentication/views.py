from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        firstname =request.POST['fname']
        lastname =request.POST['lastname']
        uname =request.POST['uname']
        password =request.POST['password']
        cpassword =request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                print("Username taken")
                messages.info(request,"same username")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                print("Error: Same email registed")
                messages.info(request,"same email")
                return redirect("register")
            else:
                user =User.objects.create_user(username=uname,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()
                print('user registed')
                messages.info(request,"User register")
                return redirect("register")
        else:
            print('user not registed')
            messages.info(request,"User not register")
            return redirect("register")
        return redirect('/')
    else:
        return render(request,'register.html')

def log(request):
    if request.method == 'POST':
        uname =request.POST['uname']
        password =request.POST['password']
        user= auth.authenticate(request, username=uname, password=password)

        if user is not None:
            auth.login(request,user)  
            print("user login")  
            return redirect("/")
        else:
            print("invalid login")
            return redirect('log')
        
    else:
        return render(request, 'login.html')

def logout_user(request):
    auth.logout(request)
    print('logout')
    return redirect('/')
   

