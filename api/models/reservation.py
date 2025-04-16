from django.db import models


class Reservation(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    spot = models.ForeignKey("ParkingSpot", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"Reservation by {self.user.username} - Active: {self.is_active}"
