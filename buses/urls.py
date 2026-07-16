from django.urls import path
from . import views

urlpatterns = [
    path("", views.bus_list, name="bus_list"),
    path("add/", views.add_bus, name="add_bus"),
    path("edit/<int:pk>/", views.edit_bus, name="edit_bus"),
    path("delete/<int:pk>/", views.delete_bus, name="delete_bus"),
]