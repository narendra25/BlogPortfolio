from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Login
# Create your views here.
def signup(request):
    if request.method=="POST":
        get_email=request.POST.get("email")
        get_password=request.POST.get("password")
        get_confirm_password=request.POST.get("confirm password")
        
        if get_password!=get_confirm_password:
            messages.info(request,"Password is Not Matching")
            return redirect("/auth/signup/")
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"Email is Taken")
                return redirect("/auth/signup/")
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(get_email,get_email,get_password)
        print(myuser)
        myuser.save()

        messages.success(request,"User is Created Please Login.....")
        return redirect("/auth/login/")
    return render(request,'signup.html')

def handlelogin(request):
    get_email=request.POST.get("email")
    get_password=request.POST.get("password")
    myuser=authenticate(username=get_email,password=get_password) 
    #query=Login(myuser)
    #query.save()
    print(myuser)
    if myuser is not None:
        login(request,myuser)
        messages.success(request,"Login successful")
        return redirect("/")
    else:
        messages.error(request,"Invalid Credential ..Plz check")
    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout successful")
    return render(request,'login.html')
