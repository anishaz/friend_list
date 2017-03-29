from django.shortcuts import render, redirect
from ..loginreg.models import User, UserManager
from . models import Friend
from django.contrib import messages

def dashboard(request):
    if not 'user' in request.session:
        return redirect('/main')

    id = request.session['user']
    print id

    data = {
        "myfriends" : User.objects.filter(friend_friendship__user=id),
        "others" : User.objects.exclude(friend_friendship__user=id) and User.objects.exclude(id=id) and User.objects.exclude(friend_friendship__user=id),
        "user" : User.objects.get(id=id)
    }

    return render(request, 'friends/friends.html', data)

def add(request, id):
    me = request.session['user']

    result = Friend.objects.addFriend(me, id)

    return redirect('/friends')

def remove(request,id):
    me = request.session['user']

    result = Friend.objects.removeFriend(me, id)

    return redirect ('/friends')

def view(request, id):
    query = User.objects.get(id=id)
    data = {
        "user" : query
    }

    return render(request, 'friends/profile.html', data)
