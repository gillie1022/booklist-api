from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Author(models.Model):
    author = models.CharField(max_length=100, unique=True)

class Book(models.Model):
    user = models.ForeignKey(to=User, on_delete=CASCADE, related_name='books')
    title = models.CharField(max_length=500)
    authors = models.ManyToManyField(to=Author, related_name='books')