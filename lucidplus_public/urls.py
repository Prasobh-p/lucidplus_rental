from django.urls import path
from lucidplus_public import views

urlpatterns = [
    path('Public_indexpage', views.Public_indexpage, name='Public_indexpage'),
    path('Owner_managmentpage',views.Owner_managmentpage,name='Owner_managmentpage'),
    path('owner_page',views.owner_page,name='owner_page'),
    path('Renterpage',views.Renterpage,name='Renterpage'),
    path('Booking_system',views.Booking_system,name='Booking_system'),
    path('signup_page',views.signup_page,name="signup_page"),
    path('Public_signup_view',views.Public_signup_view,name='Public_signup_view'),
    path('Public_login',views.Public_login,name="Public_login"),
    path('Public_entry',views.Public_entry,name='Public_entry'),
    path('Public_logout',views.Public_logout,name='Public_logout'),





]
