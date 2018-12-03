from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	# return HttpResponse("about")
	#for returning a template we have to render somting 
	#after importing render
	return render(request,"about.html")

def homepage(request):
	# return HttpResponse("Homepage")
	
	return render(request,"homepage.html")