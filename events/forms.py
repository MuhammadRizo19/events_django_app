from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'manager', 'description')
		labels = {
		    'name' : "Event Name",
		    'event_date' : "YY-MM-DD HH-MM-SS", 
		    'venue' : "Venue",
		    'manager' : "Manager",
		    'description' : "Description",
		}
		widgets = {
		    'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
		    'event_date' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'event date'}),
		    'venue' : forms.Select(attrs={'class':'form-select', 'placeholder':'venue'}),
		    'manager' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'manager'}),
		    'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'description'}), 
		}

class VenueForm(forms.ModelForm):
	class Meta:
		model = Venue
		fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address', 'venue_image')
		labels = {
		    'name' : "",
		    'address' : "", 
		    'zip_code' : "",
		    'phone' : "",
		    'web' : "",
		    'email_address' : "",
		    'venue_image':"",    
		}
		widgets = {
		    'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name', 'cols':20, 'rows':20}),
		    'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
		    'zip_code' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
		    'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
		    'web' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Site'}),
		    'email_address' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
		}