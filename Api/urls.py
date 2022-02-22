from django.contrib import admin
from django.urls import path
from . import views

app_name="Api"

urlpatterns = [
    path('', views.home,name="search"),
    path('getVedios/<str:key>/', views.getMessages, name='getV'),    
]