from django.urls import path
from . import views

urlpatterns = [
    path("", views.bus_list, name="bus_list"),
    path("add/", views.add_bus, name="add_bus"),
]