from django.contrib import admin
from django.urls import path, include
from .views import indexPage,thsPage

urlpatterns = [
    path('', indexPage, name="index"),
    path('ths', thsPage, name="ths"),
]
