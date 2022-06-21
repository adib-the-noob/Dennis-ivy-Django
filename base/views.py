from django.http import HttpResponse
from django.shortcuts import render,redirect

from base.forms import RoomForm
from .models import Room

#rooms = [{'id': 1, 'name': 'Learn Python'},
#        {'id': 2, 'name': 'Learn Java'},
#       {'id': 3, 'name': 'Learn C++'}, ]

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html',context)