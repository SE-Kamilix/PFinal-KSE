from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost, Page

admin.site.register(BlogPost)
admin.site.register(Page)
