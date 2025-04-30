from django.contrib import admin
from .models import Property,UserProfile,Booking

admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(UserProfile)

