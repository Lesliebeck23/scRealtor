from django import forms
from .models import Listing



class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ('address', 'sqft', 'bedrooms', 'bathrooms', 'description', 'home_photo', 'price')

        widgets = {
            'address': forms.TextInput(attrs = {'class': 'form-control'}),
            'added_by': forms.Select(attrs = {'class': 'form-control'}),
            'sqft': forms.TextInput(attrs = {'class': 'form-control'}),
            'bedrooms': forms.TextInput(attrs = {'class': 'form-control'}),
            'bathrooms': forms.TextInput(attrs = {'class': 'form-control'}),
            'description': forms.Textarea(attrs = {'class': 'form-control'}),
            'price': forms.TextInput(attrs = {'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ('address', 'sqft', 'bedrooms', 'bathrooms', 'description', 'home_photo', 'price')

        widgets = {
            'address': forms.TextInput(attrs = {'class': 'form-control'}),
            'added_by': forms.Select(attrs = {'class': 'form-control'}),
            'sqft': forms.TextInput(attrs = {'class': 'form-control'}),
            'bedrooms': forms.TextInput(attrs = {'class': 'form-control'}),
            'bathrooms': forms.TextInput(attrs = {'class': 'form-control'}),
            'description': forms.Textarea(attrs = {'class': 'form-control'}),
            'price': forms.TextInput(attrs = {'class': 'form-control'}),
        }


