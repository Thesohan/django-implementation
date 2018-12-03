from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.contrib.auth import login, logout


def signup_view(request):
	if request.method =='POST':
		#We gona send the data
		form = UserCreationForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			#now we will log use in
			#redirect the use to article list
			login(request,user)
			return redirect('articles:list')
	else:
		form = UserCreationForm()

	return render(request,'accounts/signup.html',{'form':form})
	#this return statement is outside the else because it will also execute
	# when request.method is post and form is not valid;

#request maybe a post request or get request
def login_view(request):
	if request.method =='POST':
		#if request i post request then the data we recevie from reqeust we have to authenticate that
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#login the user
			user = form.get_user()#it will return the user who is goinng to login
			
			login(request,user)#first argument is request and second argument is the user who wanna be login in
			
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('articles:list')
	else:
		form = AuthenticationForm()
	return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
	#we are gonna 
	if request.method =='POST':
		logout(request)#django already knows the current user
		return redirect('articles:list')
