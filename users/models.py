from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "ADMIN"
    OPERATOR = "OPERATOR"
    CUSTOMER = "CUSTOMER"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (OPERATOR, "Operator"),
        (CUSTOMER, "Customer"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER,
    )

    def __str__(self):
        return self.username