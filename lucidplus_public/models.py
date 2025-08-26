from django.db import models

class Propertydb(models.Model):
    TITLE = models.CharField(max_length=255, null=True, blank=True)
    ADDRESS = models.TextField(null=True, blank=True)
    GEOLOCATION = models.CharField(max_length=100, null=True, blank=True)
    RENT_PER_MONTH = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PROPERTY_TYPE = models.CharField(max_length=50, null=True, blank=True)
    AMENITIES = models.TextField(null=True, blank=True)
    AVAILABILITY_START = models.DateField(null=True, blank=True)
    AVAILABILITY_END = models.DateField(null=True, blank=True)
    DESCRIPTION = models.TextField(null=True, blank=True)
    PROPERTY_IMAGE = models.FileField(upload_to='property_images', null=True, blank=True)


class RentalHistorydb(models.Model):
    PROPERTY = models.ForeignKey(Propertydb, on_delete=models.CASCADE, null=True, blank=True)
    RENTER_NAME = models.CharField(max_length=255, null=True, blank=True)
    DATE_FROM = models.DateField(null=True, blank=True)
    DATE_TO = models.DateField(null=True, blank=True)
    STATUS = models.CharField(max_length=50, null=True, blank=True)

class Signupdb(models.Model):
    ROLE_CHOICES = (('Owner', 'Owner'),('Renter', 'Renter'),)
    ROLE = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    FULL_NAME = models.CharField(max_length=255, null=True, blank=True)
    EMAIL = models.EmailField(unique=True, null=True, blank=True)
    PASSWORD = models.CharField(max_length=255, null=True, blank=True)
    CONFIRMPASSWORD=models.CharField(max_length=255, null=True, blank=True)


