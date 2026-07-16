from django import forms
from .models import Bus


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = [
            "bus_number",
            "bus_name",
            "bus_type",
            "total_seats",
            "is_active",
        ]

        widgets = {
            "bus_number": forms.TextInput(attrs={"class": "form-control"}),
            "bus_name": forms.TextInput(attrs={"class": "form-control"}),
            "bus_type": forms.Select(attrs={"class": "form-select"}),
            "total_seats": forms.NumberInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }