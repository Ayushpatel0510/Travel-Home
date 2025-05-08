from django.contrib import admin
from .models import Property,UserProfile,Booking,Exclusive,Trending

admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(UserProfile)
admin.site.register(Exclusive)
admin.site.register(Trending)

