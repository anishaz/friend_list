from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'loginreg/index.html')

def register(request):
    result = User.objects.registration(request.POST.copy())

    if 'errors' in result:
        for errors in result['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect('/main')

    request.session['user'] = result['user'].id
    print request.session['user']

    return redirect ('/friends')

def login(request):
    result = User.objects.login(request.POST.copy())

    if 'errors' in result:
        for errors in result['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect ('/main')

    request.session['user'] = result['user'].id
    print request.session['user']

    return redirect('/friends')

def logout(request):
    request.session.clear()
    return redirect('/main')
