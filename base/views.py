from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def  home(request):
    return render(request, 'base/home.html')

def room(request,pk):
    rooms = [{'id':1,'name': 'Learn Pthon'},
                        {'id':2,'name': 'Learn Java'},
                        {'id':3,'name': 'Learn C++'},]
    #59.58s done
    return render(request, 'base/room.html',{'rooms':rooms})