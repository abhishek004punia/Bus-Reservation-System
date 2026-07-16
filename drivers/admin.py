from django.contrib import admin
from .models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "license_number",
        "experience",
        "is_active",
    )

    list_filter = ("is_active",)
    search_fields = ("name", "license_number", "phone")