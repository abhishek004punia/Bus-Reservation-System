from django import forms
from .models import Route


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = [
            "source",
            "destination",
            "distance",
            "duration",
        ]

        widgets = {
            "source": forms.TextInput(attrs={"class": "form-control"}),
            "destination": forms.TextInput(attrs={"class": "form-control"}),
            "distance": forms.NumberInput(attrs={"class": "form-control"}),
            "duration": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),
        }