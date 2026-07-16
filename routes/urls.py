from django.urls import path
from . import views

urlpatterns = [
    path("", views.route_list, name="route_list"),
    path("add/", views.add_route, name="add_route"),
]