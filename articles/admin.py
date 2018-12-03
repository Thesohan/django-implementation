from django.contrib import admin

# Register your models here.
from .models import Article

admin.site.register(Article) #now django knows that we want to see Article model in our Admin page