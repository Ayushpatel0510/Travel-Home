from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Property,UserProfile,Booking
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import BookingForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        address=request.POST["address"]
        pincode=request.POST["pincode"]
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user=User.objects.create_user(username=username, password=password,email=email)
            UserProfile.objects.create(user=user,address=address,mobile=mobile,pincode=pincode)
            messages.success(request, 'Account created! Please log in.')
            return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'index.html')

def listing(request):
    properties = Property.objects.all()
    return render(request, 'listing.html', {'properties': properties})

def travel(request):
    return render(request, 'travel.html')

def house_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.property = property
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('house_detail',property_id=property_id)
    else:
        form = BookingForm()

    return render(request, 'house.html', {'property': property, 'form': form})

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('property')
    return render(request, 'my_bookings.html', {'bookings': bookings})





    

    
    

