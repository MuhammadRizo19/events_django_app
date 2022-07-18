from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home.html'),
    path('<int:year>/<str:month>/', views.home, name='home.html'),
    path('events', views.all_events, name='events'),
    path('add_venue', views.add_venue, name='add_venue'), 
    path('venues', views.all_venues, name='all_venues'),
    path('show_venue/<venue_id>', views.show_venue, name='show_venue'),
    path('search_all', views.search, name='search'),
    path('edit_venue/<venue_id>', views.edit_venue, name='edit_venue'),
    path('edit_event/<event_id>', views.edit_event, name='edit_event'),
    path('add_event', views.add_event, name='add_event'), 
    path('delete_event/<event_id>', views.delete_event, name='delete_event'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete_venue'),
]