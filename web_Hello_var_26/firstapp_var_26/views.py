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

def agencies(request):
    agencies = [
        {
            "name": "1002 Тур",
            "address": "Тверская, 16",
            "phone": "+7 (495) 735-11-01",
        },
        {
            "name": "Чип Тревелс",
            "address": "Ветошный переулок, 10",
            "phone": "+7 (495) 569-23-66",
        },
        {
            "name": "Апельсин Тревелс",
            "address": "ул. Широкая, 14",
            "phone": "+7 (495) 365-32-40",
        },
    ]

    return render(request, "agencies.html", context={"agencies": agencies})

def preparation(request):
    return render(request, "preparation.html")
