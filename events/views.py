from django.shortcuts import render,redirect
import calendar
from django.contrib import messages
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, ClubUser, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.paginator import Paginator

def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	event.delete()
	return redirect('events')

def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue.delete()
	return redirect('all_venues')	

def add_event(request):
	submitted = False
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
		    form.save() 
		    return HttpResponseRedirect('/add_event?/submitted=True')

		messages.success(request, 'your venue has been added successfully')
	else:
		form = EventForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'add_event.html', {'form': form, 'submitted': submitted})		

def edit_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('events')
	return render(request, 'edit_event.html', {'event':event,'form':form})

def edit_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None,instance=venue)
	if form.is_valid():
		form.save()
		return redirect('all_venues')
	return render(request, 'edit_venue.html', {'venues':venue,'form':form})

def search(request):
	if request.method=='POST':
		searched = request.POST['searched']
		venue = Venue.objects.filter(name__contains=searched)
		event = Event.objects.filter(name__contains=searched)
		return render(request, 'searching.html', {'searched':searched, 'venues':venue, 'events':event})

	else:
	    return render(request, 'searching.html')
	
def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	return render(request, 'show_venue.html',{'venue':venue})

def all_venues(request):
	all_venues = Venue.objects.all().order_by('name')
	p = Paginator(Venue.objects.all(), 3)
	page = request.GET.get('page')
	venues = p.get_page(page)
	nums = 'a' * venues.paginator.num_pages 
	return render(request, 'list_venue.html', {'venues':venues, 'nums': nums})

def add_venue(request):
	submitted = False
	if request.method == 'POST':
		form = VenueForm(request.POST, request.FILES)
		if form.is_valid():
		    form.save() 
		    return HttpResponseRedirect('/add_venue?/submitted=True')

		messages.success(request, 'your venue has been added successfully')
	else:
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'add_venue.html', {'form': form, 'submitted': submitted})		

def all_events(request):
	events = Event.objects.all().order_by('name')
	visitorsnumber = ClubUser.objects.all().count()
	return render(request, 'event_list.html', {'events':events, 'number':visitorsnumber})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	month = month.capitalize()
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)
	cal = HTMLCalendar().formatmonth(year,month_number)
	return render(request, 'home.html', {'year': year, 'month':month,
	                                     'month_number':month_number, 'cal':cal})
