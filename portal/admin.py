from django.contrib import admin
from .models import Article, Author, Comment, Bookmark

# Register your models here.
admin.site.register([Article, Author, Comment, Bookmark])