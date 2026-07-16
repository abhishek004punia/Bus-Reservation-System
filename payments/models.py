from django.db import models
from bookings.models import Booking


class Payment(models.Model):

    PAYMENT_STATUS = [
        ("PENDING", "Pending"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="SUCCESS",
    )

    transaction_id = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.transaction_id