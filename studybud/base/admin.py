from django.contrib import admin
from .models import Room, Topic , Message

# Register your models here.

# we will do that with the help of the admin decorator

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug' : ('name',)}
    
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','host','created','updated']
    list_filter = ['name','created']
    search_fields = ['name']
    
    
@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ['user','created','updated']
    list_filter = ['user','created','updated']
    search_fields = ['user']