from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

rooms = [{'id':1,'name': 'Learn Python'},
                        {'id':2,'name': 'Learn Java'},
                        {'id':3,'name': 'Learn C++'},]

# Create your views here.
def  home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html',context)