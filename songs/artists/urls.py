from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="artists-home"),
    path('songs/', views.song, name="artists-song"),

    

]
