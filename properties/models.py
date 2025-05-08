from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to="owner/",null=True,blank=True)
    mobile = models.CharField( max_length=10)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    is_host = models.BooleanField(default=False)
    
class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner=models.CharField(max_length=50)
    owner_pic=models.ImageField(upload_to="owner/")
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    location_embed = models.TextField(blank=True, null=True)
    description = models.TextField()
    property_type = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    max_guests = models.PositiveIntegerField()
    image = models.ImageField(upload_to="properties/")
    rating = models.FloatField(default=0.0)
    reviews=models.PositiveIntegerField(default=0)
    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.location = self.location.title()
        self.property_type = self.property_type.title()
        super(Property, self).save(*args, **kwargs)
    

    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    booking_time=models.DateTimeField(auto_now_add=True)

class Exclusive(models.Model):
    image=models.ImageField(upload_to="exclusive/")
    name=models.TextField()
    starts_at=models.PositiveIntegerField(default=1000)
    
class Trending(models.Model):
    image=models.ImageField(upload_to="trending")
    name=models.TextField()
    