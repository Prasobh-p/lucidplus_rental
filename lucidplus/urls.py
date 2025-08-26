from django.urls import path
from lucidplus import views


urlpatterns = [
    path('Basepage',views.Basepage,name='Base'),
    path('Indexpage', views.Indexpage, name='Indexpage'),

    path('propertypage',views.propertypage,name='propertypage'),
    path('booking',views.Booking,name='Booking'),
    path('Flagged',views.Adminlaggedpage,name='Flagged'),
    path('Loginpage',views.Loginpage,name='Loginpage'),
    path('Adminlogin',views.Adminlogin,name='Adminlogin'),
    path('Adminlogout',views.Adminlogout,name='Adminlogout'),





]