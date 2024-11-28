from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Room
from .form import RoomForm

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
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)




# views for updating new form
def updateForm(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    context = {'form':form}
    return render(request,'base/room_form.html',context)