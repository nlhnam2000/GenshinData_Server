from django.urls import path
from . import views

urlpatterns = [
    path('characters', views.getCharacter), 
    path('login', views.login)
]