from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "passenger_name",
        "schedule",
        "seat_number",
        "status",
        "booking_date",
    )

    list_filter = ("status",)
    search_fields = (
        "passenger_name",
        "mobile_number",
    )