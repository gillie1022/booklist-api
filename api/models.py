from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class User(AbstractUser):
    pass

class Author(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

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
    
class Note(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="notes", null=True, blank=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    page_number = models.PositiveIntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']