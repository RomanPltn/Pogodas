from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name="home"),
    path('logint/', views.logint, name="logint"),
    path('registr/', views.registr, name="registr"),
    path('logout/', views.exit, name="logout"),
    path('', views.entry, name="entry")
]
