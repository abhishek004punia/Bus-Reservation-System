from django.db import models

# Create your models here.


class Route(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["source", "destination"]

    def __str__(self):
        return f"{self.source} → {self.destination}"