from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Room , Topic
from .form import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

# login page
def loginPage(request):
    if request.method == "POST":
        # get the user cred from the user
        username = request.POST.get('username')
        password = request.POST.get('password')
        # get this from the database
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist.')
        # authenticate the user from the django    
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            # login using the post method
            login(request,user)
            return redirect('base:home')
        else:
            messages.error(request,'Username or Password does not match!!')
    context = {}
    return render(request,'base/login_registration.html',context)


# logout view
def logoutPage(request):
    logout(request)
    return redirect('base:home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # filtering out the room using the topic name,name ,host username or desc
    room = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(desc__icontains=q) |
        Q(host__username__icontains=q)
        )
    # build the context var
    room_count = room.count() # room count
    topic = Topic.objects.all()
    context = {'room':room,'topic':topic,'room_count':room_count}
    return render(request,'base/home.html',context)

def room(request,pk):
    # querying from the room table using the id
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)



# views for creating new form
@login_required(login_url='base:login')
def createRoom(request):
    
    # create the room from the form.py meta model using the post method
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)




# views for updating new form
@login_required(login_url='base:login')
def updateRoom(request,pk):
    # create the room from the form.py meta model using the post method
    room = Room.objects.get(id=pk)
    #checking the instance from the model
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        # restricting the user from the op.
        return HttpResponse("You are not allowed here!!")
    if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        form.save()
        return redirect('base:home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)


# views for delete the form
@login_required(login_url='base:login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request,'base/delete.html',{'obj':room})