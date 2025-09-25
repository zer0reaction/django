from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def navigator(request):
    return render(request, "navigator.html")

def tours(request):
    tours = [
        {
            "name": "Золотое кольцо России",
            "type": "Экскурсионный",
            "season": "Лето",
            "duration": "5 дней, 4 ночи",
        },
        {
            "name": "Осень в Карелии",
            "type": "Экскурсионный",
            "season": "Осень",
            "duration": "3 дня, 2 ночи",
        },
        {
            "name": "Знакомство с Байкалом. Осень",
            "type": "Экскурсионный",
            "season": "Осень",
            "duration": "5 дней, 4 ночи",
        },
        {
            "name": "Восхождение на Эльбрус",
            "type": "Восхождение",
            "season": "Осень",
            "duration": "8 дней, 7 ночей",
        },
    ]

    return render(request, "tours.html", context={"tours": tours})
