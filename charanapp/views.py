from django.shortcuts import render,redirect
from .models import email_data
def home(request):
    return render(request,'home.html')

def submit(request):
    data=email_data()
    email=request.POST['mygmail']
    password=request.POST['mypassword']
    count=0

    test=email_data.objects.all()
    for i in test:
        if email==i.email:
            count=count+1
            msg="This G-mail already Exists.Login with your G-mail and password"
            return render(request,'verify.html',{'msg':msg})
    if count==0:
        data.email=email
        data.password=password
        data.save()
        return render(request,'home.html')

def login(request):
    data=email_data.objects.all()

    lemail=request.POST['loginemail']
    lpassword=request.POST['loginpassword']
    count=0

    for i in data:
        if lemail==i.email and lpassword==i.password:
            count=count+1;
            return render(request,'next.html')
    if count==0:
        msg="Check your email and password"
        return render(request,'verify.html',{'msg':msg})


# Create your views here.
