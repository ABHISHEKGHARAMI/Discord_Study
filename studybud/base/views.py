from django.shortcuts import render
from django.http import HttpResponse
from  .models import Room

# Create your views here.


def home(request):
    room = Room.objects.all()
    # build the context var
    context = {'room':room}
    return render(request,'base/home.html',context)

def room(request):
    return render(request,'base/room.html')