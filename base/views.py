from re import L
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm 

# Create your views here.

def home(request):  
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room (request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm() # init form with fields in the form.py from its model

    if request.method == 'POST':
        form = RoomForm(request.POST) ## fill it with the values from the request
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk) # query the room
    form = RoomForm(instance=room) # prefill the data

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) ## tell it which room to update, so the instance ix the room with prefilled data
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})