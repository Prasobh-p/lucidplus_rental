from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def Basepage(req):
    return render(req,'Base.html')

def Indexpage(req):
    return render(req,'Index_page.html')

def propertypage(req):
    return render(req,'Property_page.html')

def Booking(req):
    return render(req,'Booking.html')

def Adminlaggedpage(req):
    return render(req,'Flagged.html')


def Loginpage(req):
    return render(req,'Publicsignup_page.html')



def Adminlogin(req):
    if req.method == "POST":
        un = req.POST.get("username")
        pas = req.POST.get("pass")
        if User.objects.filter(username__contains=un).exists():
            x= authenticate(username=un,password=pas)
            if x is not None :
                login(req,x)
                req.session['username']=un
                req.session['password']=pas
                return redirect(Indexpage)
            else:
                return redirect(Loginpage)

        else:
            return redirect(Loginpage)


def Adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(Loginpage)
