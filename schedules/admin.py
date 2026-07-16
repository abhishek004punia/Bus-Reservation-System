from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "bus",
        "route",
        "driver",
        "travel_date",
        "departure_time",
        "fare",
        "available_seats",
        "is_active",
    )

    list_filter = (
        "travel_date",
        "is_active",
    )

    search_fields = (
        "bus__bus_name",
        "route__source",
        "route__destination",
    )