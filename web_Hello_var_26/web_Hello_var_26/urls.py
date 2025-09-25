"""
URL configuration for web_Hello_var_26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from firstapp_var_26 import views

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

urlpatterns = [
    path('', views.index),
    path('navigator', views.navigator),
    re_path(r'^[Tt]ours?$', views.tours, kwargs={"tours": tours}),
    re_path(r'^[Aa]gencies$', views.agencies, kwargs={"agencies": agencies}),
    re_path(r'^[Pp]reparation$', views.preparation),
    path('admin/', admin.site.urls),
]
