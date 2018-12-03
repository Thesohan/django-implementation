from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
# Create your views here.
# def article_list(request):
# 	return render(request,"articles/article_list.html")

from .models import Article
from django.http import HttpResponse

from .import forms
def article_list(request):
	articles = Article.objects.all().order_by('date')# this method will return all the Article objects
	# and order them by the passed argument (field present in Article object)
	#now we are going to send all the fetched articles to our template
	return render(request,'articles/article_list.html',{ 'articles' : articles })
	#{ 'articles' : articles } it is a dictionary

def article_detail(request,slug):
	# return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			#save this into db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect("articles:list")
	else:
		form = forms.CreateArticle()
	return render(request,'articles/article_create.html',{'form':form})
