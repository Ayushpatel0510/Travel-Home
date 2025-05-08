from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Property,UserProfile,Booking,Exclusive,Trending
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import BookingForm,PropertyForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q
from django.core.paginator import Paginator
from math import floor


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        address=request.POST["address"]
        pincode=request.POST["pincode"]
        is_host = 'is_host' in request.POST
        profile_picture=request.FILES.get("profile_picture")
        
        if password != cpassword:
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect('login')
        else:
            user=User.objects.create_user(username=username, password=password,email=email,first_name=firstname,last_name=lastname)
            UserProfile.objects.create(user=user,address=address,mobile=mobile,pincode=pincode,is_host=is_host,profile_picture=profile_picture)
            messages.success(request, 'Account created! Please log in.')
            return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginas=request.POST.get('loginas')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if loginas == 'host':
                if user.userprofile.is_host:
                    login(request, user)
                    messages.success(request, 'Login Successfull')
                    return redirect('host_dashboard')
                
                else:
                    messages.warning(request, 'You are not a host')    
                    return redirect('login')
            else:
                login(request, user)
                messages.success(request, 'Login Successfull')
                return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfull')
    
    return redirect('home')

def home(request):
    trending=Trending.objects.all()
    exclusive=Exclusive.objects.all()
    return render(request, 'index.html',{'trending':trending ,'exclusive':exclusive})

def host_dashboard(request):
    return render(request, 'host_dashboard.html')

def listing(request):
    properties = Property.objects.all()
    query = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    guests = request.GET.get('guests')
    min_rating = request.GET.get('min_rating')
    category = request.GET.get('category')
    categories = Property.objects.values_list('property_type', flat=True).distinct()
    loc_q = request.GET.get('loc_q', '')
    gue_q = request.GET.get('gue_q', '')
    sort_by = request.GET.get('sort_by')
    
    if loc_q:
        properties = Property.objects.filter(
            Q(location__icontains=loc_q)
        )
        loc_q=loc_q.title()
        if gue_q:
            gue_q = int(gue_q)
            properties = properties.filter(max_guests__gte=gue_q)
    # seaching logic
    if query:
        properties = properties.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(location__icontains=query)
    )
        
    if min_price:
        properties = properties.filter(price_per_day__gte=min_price)

    if max_price:
        properties = properties.filter(price_per_day__lte=max_price)

    if guests:
        properties = properties.filter(max_guests__gte=guests)

    if min_rating:
        properties = properties.filter(rating__gte=min_rating)
    if category:
        properties = properties.filter(property_type=category)
        
    # sorting logic   
    if sort_by == 'price_asc':
        properties = properties.order_by('price_per_day')
    elif sort_by == 'price_desc':
        properties = properties.order_by('-price_per_day')
    elif sort_by == 'rating_desc':
        properties = properties.order_by('-rating')
    elif sort_by == 'rating_asc':
        properties = properties.order_by('rating')
    
    # rating star logic
    for prop in properties:
        rating = prop.rating or 0
        full = int(floor(rating))
        half = 1 if rating - full >= 0.5 else 0
        empty = 5 - full - half
        prop.star_data = {
            'full': range(full),
            'half': range(half),
            'empty': range(empty)
        }
    paginator = Paginator(properties, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listing.html', {'properties': page_obj,'categories': categories,'loc_q': loc_q})



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
        
    if property:
        rating = property.rating or 0
        full = int(floor(rating))
        half = 1 if rating - full >= 0.5 else 0
        empty = 5 - full - half
        property.star_data = {
            'full': range(full),
            'half': range(half),
            'empty': range(empty)
        }
    return render(request, 'house.html', {'property': property, 'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('property')
    paginator = Paginator(bookings, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'my_bookings.html', {'bookings': page_obj})

@login_required
def my_properties(request):
    properties = Property.objects.filter(owner=request.user)
    paginator = Paginator(properties, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'my_properties.html', {'properties': page_obj})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, 'Your booking has been cancelled.')
    return redirect('my_bookings')



@login_required
def add_property(request):
    if not request.user.userprofile.is_host:
        return HttpResponseForbidden("Only hosts can add properties.")
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user 
            property.owner = request.user
            property.owner_pic=request.user.userprofile.profile_picture
            property.save()
            messages.success(request, "Property added successfully!")
            return redirect('my_properties')
    else:
        form = PropertyForm()

    return render(request, 'add_property.html', {'form': form})


@login_required
def edit_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id, owner=request.user)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            messages.success(request, "Property edited successfully!")
            return redirect('my_properties')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'edit_property.html', {'form': form})

@login_required
def delete_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id, owner=request.user)
    property.delete()
    messages.success(request, "Property deleted successfully!")
    return redirect('my_properties') 

@login_required
def register_as_host(request):
    profile = request.user.userprofile
    if not profile.is_host:
        profile.is_host = True
        profile.save()
        messages.success(request, "You are now registered as a host!")
    else:
        messages.info(request, "You are already a host.")
    return redirect('home') 

