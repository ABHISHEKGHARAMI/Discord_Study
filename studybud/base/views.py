from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Room , Topic
from .form import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# login page
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist.')
            
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('base:home')
        else:
            messages.error(request,'Username or Password does not match!!')
    context = {}
    return render(request,'base/login_registration.html',context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    room = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(desc__icontains=q) |
        Q(host__username__icontains=q)
        )
    # build the context var
    room_count = room.count()
    topic = Topic.objects.all()
    context = {'room':room,'topic':topic,'room_count':room_count}
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