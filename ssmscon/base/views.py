from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.template import context
from .models import Message, Room, Student, Topic
from .forms import RoomForm, EditProfile
import sys

# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Does Not Exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login (request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Incorrect')
    context = {'page' : page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An Error Has Occured')

    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topic = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms' : rooms, 'topics' : topic, 'room_count' : room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')

    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room':room, 'room_messages': room_messages, 'participants':participants}
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form  = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed to do that')

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed to do that')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed to do that')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':message})

@login_required(login_url='login')
def profilePage(request):
    
    student = Student.objects.get(user_id=request.user.id)
    # print(student, file=sys.stderr)
    context = {'student':student}

    return render(request, 'base/profilepage.html', context)

@login_required(login_url='login')
def editProfile(request):
    student = Student.objects.get(user_id=request.user.id)
    form = EditProfile(instance=student)

    # if request.user != student.user_id:
    #     return HttpResponse('You are not allowed to do that')

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profilepage')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def connect4(request):
    context = {}
    return render(request, 'base/connect4.html', context)

def snake(request):
    context = {}
    return render(request, 'base/snake.html', context)

def tictactoe(request):
    context = {}
    return render(request, 'base/tictactoe.html', context)

