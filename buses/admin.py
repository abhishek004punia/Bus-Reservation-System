from django.contrib import admin
from .models import Bus

# Register your models here.

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = (
        "bus_number",
        "bus_name",
        "bus_type",
        "total_seats",
        "is_active",
    )

    list_filter = ("bus_type", "is_active")
    search_fields = ("bus_number", "bus_name")