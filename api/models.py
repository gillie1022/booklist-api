from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Author(models.Model):
    author = models.CharField(max_length=100, unique=True)

class Book(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    authors = models.ManyToManyField(to=Author, related_name='books')
    TO_READ = 'to read'
    READING = 'reading'
    READ = 'read'
    STATUS_CHOICES = [
        (TO_READ, 'to read'),
        (READING, 'reading'),
        (READ, 'read')
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=TO_READ)