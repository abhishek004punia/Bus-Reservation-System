from django.db import models
from buses.models import Bus
from routes.models import Route
from drivers.models import Driver


class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    travel_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    fare = models.DecimalField(max_digits=8, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.bus} | {self.route} | {self.travel_date}"