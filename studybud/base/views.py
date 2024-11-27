from django.shortcuts import render
from django.http import HttpResponse
from  .models import Room

# Create your views here.


def home(request):
    room = Room.objects.all()
    # build the context var
    
    return render(request,'home.html',{'room':room})

def room(request):
    return render(request,'room.html')