import re
from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        'dojos' : Dojo.objects.all()
    }
    return render (request, 'index.html', context)

def add_ninja(request, id):
    context = {
        'dojo' : Dojo.objects.get(id = id)
    }
    if request.method == 'GET':
        return render (request, 'add_ninja.html', context)
    if request.method == 'POST':
        id = Dojo.objects.get(id=int(request.POST['dojo']))
        Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo = id)
        return redirect ('/')

def add_dojo(request):
    Dojo.objects.create(name= request.POST["name"])
    return redirect ('/')

def dojo_members(request, id):
    context = {
        'dojo' : Dojo.objects.get(id = id),
    }
    return render (request, 'dojo_members.html', context)

def delete_dojo(request, id):
    if request.method == 'GET':
        dojo = Dojo.objects.get(id=id)
        dojo.delete()
        return redirect('/')

def delete_ninja(request, id):
    if request.method == 'GET':
        ninja = Ninja.objects.get(id=id)
        ninja.delete()
        return redirect('/')