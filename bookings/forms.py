from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "passenger_name",
            "passenger_age",
            "passenger_gender",
            "mobile_number",
            "seat_number",
        ]

        widgets = {
            "passenger_name": forms.TextInput(attrs={"class": "form-control"}),
            "passenger_age": forms.NumberInput(attrs={"class": "form-control"}),
            "passenger_gender": forms.Select(attrs={"class": "form-select"}),
            "mobile_number": forms.TextInput(attrs={"class": "form-control"}),
            "seat_number": forms.NumberInput(attrs={"class": "form-control"}),
        }