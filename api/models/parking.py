from django.db import models

# Parking Spot Model


class ParkingSpot(models.Model):
    spot_id = models.CharField(max_length=10, unique=True)
    is_occupied = models.BooleanField(default=False)
    has_charger = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return (
            f"Spot {self.spot_id} - {'Reserved' if self.is_occupied else 'Available'}"
        )
