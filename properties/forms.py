from django import forms
from .models import Booking,Property

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'guests']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'guests': forms.NumberInput(attrs={'min': 1}),
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'location','location_embed','property_type','bedrooms','bathrooms','max_guests', 'price_per_day', 'image'] 
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter property name'
            }),
            'property_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter property name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your property'
            }),
            'price_per_day': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'bedrooms': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'bathrooms': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'max_guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'
            }),
            
            'location_embed': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Enter Map location embed link'}),
            
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

        }