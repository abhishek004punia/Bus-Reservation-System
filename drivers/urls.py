from django.urls import path
from . import views

urlpatterns = [
    path("", views.driver_list, name="driver_list"),
    path("add/", views.add_driver, name="add_driver"),
]
