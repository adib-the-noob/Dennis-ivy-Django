from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

rooms = [{'id': 1, 'name': 'Learn Python'},
         {'id': 2, 'name': 'Learn Java'},
         {'id': 3, 'name': 'Learn C++'}, ]

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
