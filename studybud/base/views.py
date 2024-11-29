from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Room , Topic
from .form import RoomForm

# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    room = Room.objects.filter(topic__name__icontains=q)
    # build the context var
    topic = Topic.objects.all()
    context = {'room':room,'topic':topic}
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
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        form.save()
        return redirect('base:home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)


# views for delete the form
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request,'base/delete.html',{'obj':room})