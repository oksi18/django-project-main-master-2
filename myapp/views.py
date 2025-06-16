from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.db import models
from .models import *
from .forms import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        # Обробка логів (взяти/повернути ключ)
        if 'submit_logs' in request.POST:
            name = request.POST.get('name')
            number = request.POST.get('number')
            action = request.POST.get('action')

            if name and number and action:
                Logs.objects.create(name=name, number=number, action=action)
                return redirect('home')

        # Обробка повідомлення
        elif 'submit_message' in request.POST:
            email = request.POST.get('email')
            text = request.POST.get('text')

            if email and text:
                Message.objects.create(email=email, text=text)
                return redirect('home')

    return render(request, "home.htm")


def logs(request):
    data1 = Logs1.objects.all()
    data = {
       "Logs": data1,
    }
    return render(request, "logs.htm", data)


def list(request):
    data2 = Cabinets.objects.all()
    data = {
       "Cabinets": data2,
    }
    return render(request, "list.htm", data)

