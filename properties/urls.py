from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('host/', views.host_dashboard, name='host_dashboard'),
    path('listing/', views.listing, name='listing'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('property/<int:property_id>/', views.house_detail, name='house_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('my-properties/', views.my_properties, name='my_properties'),
    path('add_property/', views.add_property, name='add_property'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('property/edit/<int:property_id>/', views.edit_property, name='edit_property'),
    path('property/delete/<int:property_id>/', views.delete_property, name='delete_property'),
    path('become-a-host/', views.register_as_host, name='register_as_host'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
