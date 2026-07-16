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


class SearchForm(forms.Form):
    source = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Source"
        })
    )

    destination = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Destination"
        })
    )

    travel_date = forms.DateField(
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date"
        })
    )