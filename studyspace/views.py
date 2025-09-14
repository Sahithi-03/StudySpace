from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.views.decorators.csrf import csrf_protect
import json
import requests



def index(request):
    if request.user.is_authenticated:
        Ic = len(Info.objects.filter(user=request.user))
        Tc = len(Tasks.objects.filter(user=request.user))
        cc = len(Tasks.objects.filter(user=request.user, is_active=False))
        yc = len(Tasks.objects.filter(user=request.user, is_active=True))
        return render(request, 'studyspace/index.html', {
            'Ic': Ic,
            'Tc': Tc,
            'cc':cc,
            'yc':yc
        })
    else:
        return render(request, 'studyspace/index.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "studyspace/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "studyspace/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "studyspace/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "studyspace/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "studyspace/register.html")


def add(request):
    return render(request, 'studyspace/add.html', {
        't': True
    })

def save(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        txt = data['txt']
        item_d = data.get('id')
        if item_d:
            obj = Info.objects.get(id=item_d)
            obj.title = title
            obj.txt = txt
            obj.save()
        else:
            new_object = Info(user=request.user, title=title, txt=txt)
            new_object.save()
        #response_data = {'message': 'Data received successfully!', 'received_data': data}
        return JsonResponse({
            "status": "success",
            "redirect_url": reverse('list') 
            })
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    
def list(request):
    l = Info.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'studyspace/list.html', {
            'l':l
        })


def delete(request, item_id):
    I = Info.objects.get(id=item_id)
    I.delete()
    return HttpResponseRedirect(reverse('list'))

def watch(request):
    return render(request, 'studyspace/stopwatch.html')

def display(request, item_id):
    I = Info.objects.get(id=item_id)
    return render(request,'studyspace/display.html', {
        'I':I
    })

def edit(request,item_id):
    I = Info.objects.get(id=item_id)
    return render(request, 'studyspace/add.html', {
        't': I
    })

def task(request):
    T = Tasks.objects.filter(user=request.user, is_active = True).order_by('-created_at')
    C = Tasks.objects.filter(user=request.user, is_active = False).order_by('-created_at')
    return render(request, "studyspace/task.html", {
        'T': T,
        'C': C
    })

def save_t(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        item_d = data.get('id')
        if item_d:
            obj = Tasks.objects.get(id=item_d)
            obj.name = title
            obj.save()
        else:
            new_object = Tasks(user=request.user, name=title)
            new_object.save()
        return JsonResponse({
            "status": "success",
            "redirect_url": reverse('task') 
            })
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    
def check(request, task_id):
    obj = Tasks.objects.get(id=task_id)
    if obj.is_active is True:
        obj.is_active = False
        obj.save()
    else:
        obj.is_active = True
        obj.save()
    return HttpResponseRedirect(reverse('task'))

def delete_task(request, task_id):
    obj = Tasks.objects.get(id=task_id)
    obj.delete()
    return HttpResponseRedirect(reverse('task'))


def quotes(request):
    return render(request, 'studyspace/quotes.html')

