from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    name = models.CharField('Name', max_length=100)
    author = models.ForeignKey("Author", related_name='articles', on_delete=models.CASCADE)
    publication_date = models.DateTimeField('PublicationDate', auto_now=False, auto_now_add=False)
    tags = models.CharField('Tags', max_length=400)
    content = models.TextField('Text')
    views = models.IntegerField('Views', default=0)

    class Meta:
        ordering = ['publication_date', 'author', 'tags']

    def __str__(self):
        return f'{self.name} ; {self.author}'
    

class Author(models.Model):
    name = models.CharField('Name', max_length=100)
    registration_date = models.DateTimeField('RegistrationDate', auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.name}'
    

class Comment(models.Model):
    content = models.TextField('Text')
    article = models.ForeignKey("Article", related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.article} ; {self.user}'
    

class Bookmark(models.Model):
    article = models.ForeignKey("Article", related_name='bookmarks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.user} / {self.article}'    