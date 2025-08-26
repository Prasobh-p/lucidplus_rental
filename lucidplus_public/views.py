from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Propertydb, Signupdb
from django.contrib.auth.models import User


# Create your views here.

def Public_indexpage(req):
    return render(req, 'Public_index.html')


def Owner_managmentpage(req):
    return render(req, 'Owners_Management.html')


def owner_page(request):
    if request.method == 'POST':
        title = request.POST.get('TITLE')
        address = request.POST.get('ADDRESS')
        geolocation = request.POST.get('GEOLOCATION')
        rent = request.POST.get('RENT_PER_MONTH')
        property_type = request.POST.get('PROPERTY_TYPE')
        amenities = request.POST.get('AMENITIES')
        start = request.POST.get('AVAILABILITY_START')
        end = request.POST.get('AVAILABILITY_END')
        description = request.POST.get('DESCRIPTION')
        image = request.FILES.get('PROPERTY_IMAGE')

        Propertydb.objects.create(
            TITLE=title,
            ADDRESS=address,
            GEOLOCATION=geolocation,
            RENT_PER_MONTH=rent,
            PROPERTY_TYPE=property_type,
            AMENITIES=amenities,
            AVAILABILITY_START=start,
            AVAILABILITY_END=end,
            DESCRIPTION=description,
            PROPERTY_IMAGE=image
        )
        return redirect('owner_page')

    data = Propertydb.objects.all()
    return render(request, 'Owners_Management.html', {'data': data})


def Renterpage(req):
    property = Propertydb.objects.all()
    return render(req, 'Renters.html', {'data': property})  # Changed to 'data'


def Booking_system(req):
    return render(req, 'Booking_system.html')


def signup_page(req):
    return render(req, 'Publicsignup_page.html')

def Public_signup_view(request):
    if request.method == "POST":
        role = request.POST.get("role")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('Public_signup')

        # Check if email already exists
        if Signupdb.objects.filter(EMAIL=email).exists():
            messages.error(request, "Email already exists")
            return redirect('Public_signup')

        # Check if username already exists
        if Signupdb.objects.filter(FULL_NAME=full_name).exists():
            messages.error(request, "Username already taken")
            return redirect('Public_signup')

        # Save the user directly with plain password + confirm password
        Signupdb.objects.create(
            ROLE=role,
            FULL_NAME=full_name,
            EMAIL=email,
            PASSWORD=password1,
            CONFIRMPASSWORD=password2
        )

        messages.success(request, "Signup successful, please login")
        return redirect('Public_login')

    return render(request, "Publicsignup_page.html")


def Public_login(req):
    return render(req, "Public_loginpage.html")


def Public_entry(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Signupdb.objects.get(EMAIL=email)
            if password == user.PASSWORD:  # Plain text comparison
                request.session["EMAIL"] = user.EMAIL
                return redirect("Public_indexpage")
            else:
                messages.error(request, "Invalid password")
        except Signupdb.DoesNotExist:
            messages.error(request, "User does not exist")

        return redirect("Public_login")

    return render(request, "Public_loginpage.html")


def Public_logout(req):
    del req.session['email']
    del req.session['password']
    return redirect(Public_login)

