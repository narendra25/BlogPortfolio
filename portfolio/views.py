from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contacts


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fphonenumber=request.POST.get("num")
        fdescription=request.POST.get("Description")

        print(fname,femail,fphonenumber,fdescription)
        messages.info(request,f'The name is {fname},email is {femail},Phonenumber is{fphonenumber}&your query is{fdescription}')

        query=Contacts(name=fname,email=femail,phonenumber=fphonenumber,description=fdescription)
        query.save()
        messages.success(request,"Thanks For Contating us")

       
    return render(request,'contact.html')
def handleblog(request):
    return render(request,'handleblog.html')