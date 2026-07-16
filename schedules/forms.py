from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            "bus",
            "route",
            "driver",
            "travel_date",
            "departure_time",
            "arrival_time",
            "fare",
            "available_seats",
            "is_active",
        ]

        widgets = {
            "bus": forms.Select(attrs={"class": "form-select"}),
            "route": forms.Select(attrs={"class": "form-select"}),
            "driver": forms.Select(attrs={"class": "form-select"}),
            "travel_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "departure_time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time"
            }),
            "arrival_time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time"
            }),
            "fare": forms.NumberInput(attrs={"class": "form-control"}),
            "available_seats": forms.NumberInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }