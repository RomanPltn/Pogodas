import requests
from .models import City
from .forms import CityForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def home(request):
    return render(request, "users/home.html")


def logint(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return redirect("/")
    return render(request, "users/logints.html")


def registr(request):
    if request.POST:
        new_user = User(username=request.POST['username'])
        new_user.set_password(request.POST['password'])
        new_user.save()
        login(request, new_user)
        return redirect("/home")
    return render(request, "users/registr.html")


def exit(request):
    logout(request)
    return redirect("/home")


def entry():
    return redirect("/")


def index(request):
    appid = 'bfde6cab4da38de4cfbc3a5c01844f43'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]

        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'pogoda/index.html', context)
