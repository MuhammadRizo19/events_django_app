from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'you logged successfully !')
			return redirect('home.html')
		else:
		    messages.success(request, 'there is an error in logging, please try again ... ')
		    return redirect('login_user')

	else:
	    return render(request, 'login.html', {})	    	

def logout_user(request):
    logout(request) 
    return redirect('home.html')
	    
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, 'You signed up successfully')
		return redirect('home.html')
	else:
	    form = UserCreationForm()
	    return render(request, 'register.html', {'form':form})	    