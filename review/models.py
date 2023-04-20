from django.db import models

# Create your models here.

class user(models.Model):
    ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('user', 'User'),
)
    username = models.CharField(max_length=30, unique=True,default='pavan')
    email = models.EmailField(default='user@gmail.com',unique=True)
    name = models.CharField(max_length=100,default='pavan')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    def __str__(self):
        return self.username

class review(models.Model):
    username = models.CharField(max_length=30,default='pavan')
    title = models.CharField(max_length=30,default="some title")
    product_url = models.TextField(default="some content")
    def __str__(self):
        return self.username

