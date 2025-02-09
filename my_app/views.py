from lib2to3.fixes.fix_input import context

from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'Java'},
    {'id': 3, 'name': 'JS'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'my_app/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'my_app/room.html', context)