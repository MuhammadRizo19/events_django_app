from django.db import models
  

class Venue(models.Model):
    name = models.CharField('Venue name', max_length=100)
    address = models.CharField('address', max_length=30)
    zip_code = models.CharField('zip code', max_length=10) 
    phone = models.CharField('Contact Phone', max_length=12, blank=True)
    web = models.URLField('Website address', blank=True)
    email_address = models.EmailField('Email address', blank=True )
    owner = models.IntegerField('venue owner', blank=False, default=1)
   
    def __str__(self):
	    return self.name

class ClubUser(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField('User Email')

	def __str__(self):
		return self.first_name #+ ' ' + self.last_name

class Event(models.Model):
	name = models.CharField('Event Name', max_length=100)
	event_date = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, null=True,on_delete=models.CASCADE)
	manager = models.CharField('Event Manager', max_length=100)
	description = models.TextField(blank=True)
	visitors = models.ManyToManyField(ClubUser, blank=True)

	def __str__(self):
		return self.name
