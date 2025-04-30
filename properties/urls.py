from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('listing/', views.listing, name='listing'),
    path('travel/', views.travel, name='travel'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('property/<int:property_id>/', views.house_detail, name='house_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
