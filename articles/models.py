from django.db import models

from django.contrib.auth.models import User

#make sure to follow always run these commands whenever you cretate a model
#1- python manage.py makemigrations
#2- python manage.py migrate

# Create your models here.
#inherrintg properties from the models.Model
class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)#when an article is created it will automatically update the time
	thumb = models.ImageField(default='default.jpg',blank=True)
	#add in thumbnail later
	#add in author later
	author = models.ForeignKey(User,on_delete=None,default=None)


#now stirng version or an article will show the title of the article
	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50]+"..."