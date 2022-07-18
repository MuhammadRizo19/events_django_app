from django.contrib import admin
from .models import Venue, ClubUser, Event

#admin.site.register(Event)
admin.site.register(Venue)
#admin.site.register(ClubUser)

@admin.register(ClubUser)
class ClubUserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	ordering = ['first_name']
	search_fields = ('first_name', 'last_name')

@admin.register(Event)
class ClubUserAdmin(admin.ModelAdmin):
	list_display = ('name', 'event_date','venue')
	ordering = ['name']
	search_fields = ('name', 'event_date')

admin.site.site_header = 'Muhammadrizo Club'
admin.site.site_title = 'Control page'
admin.site.index_title = 'Welcome to control area...'