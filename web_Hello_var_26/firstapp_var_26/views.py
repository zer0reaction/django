from django.http import HttpResponse
from django.shortcuts import render

import json

tours_data = None
agencies_data = None

with open('firstapp_var_26/table/tours.json') as file:
    tours_data = json.load(file)

with open('firstapp_var_26/table/agencies.json') as file:
    agencies_data = json.load(file)

def index(request):
    return render(request, "index.html")

def navigator(request):
    return render(request, "navigator.html")

def tours(request):
    return render(request, "tours.html", context={"tours": tours_data})

def agencies(request):
    return render(request, "agencies.html", context={"agencies": agencies_data})

def preparation(request):
    return render(request, "preparation.html")
