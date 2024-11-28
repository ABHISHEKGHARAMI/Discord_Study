from django.shortcuts import render
from django.http import HttpResponse
from  .models import Room

# Create your views here.


def home(request):
    room = Room.objects.all()
    # build the context var
    context = {'room':room}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)



# views for creating new form
def createRoom(request):
    context = {}
    return render(request,'base/room_form.html',context)