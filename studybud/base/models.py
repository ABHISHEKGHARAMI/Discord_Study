from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 3rd model for the topic
class Topic(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    

# first model for the room
class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=250)
    desc = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']
    
    
    def __str__(self):
        return self.name
    
    
    
# 2nd model for the message
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created','-updated']
        
    def __str__(self):
        return self.body[0:50]
    
    
    
