from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_list, name="booking_list"),
    path("create/<int:schedule_id>/", views.create_booking, name="create_booking"),
    path("search/", views.search_bus, name="search_bus"),
    path("detail/<int:pk>/", views.booking_detail, name="booking_detail"),
    path("ticket/<int:pk>/pdf/", views.download_ticket, name="download_ticket"),
]