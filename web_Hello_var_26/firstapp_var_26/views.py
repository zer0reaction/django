from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def navigator(request):
    return render(request, "navigator.html")

def tours(request, tours):
    return render(request, "tours.html", context={"tours": tours})

def agencies(request, agencies):
    return render(request, "agencies.html", context={"agencies": agencies})

def preparation(request):
    return render(request, "preparation.html")
