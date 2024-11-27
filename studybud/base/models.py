from django.db import models

# Create your models here.

# first model for the room
class Room(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
