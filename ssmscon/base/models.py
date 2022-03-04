from typing import OrderedDict
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    thumb = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name 


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    speciality = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    profpic = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name