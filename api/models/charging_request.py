from django.db import models


# Charging Request Model
class ChargingRequest(models.Model):
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    spot = models.ForeignKey("ParkingSpot", on_delete=models.DO_NOTHING)
    bot_id = models.IntegerField(default=1, null=True, blank=True)
    car_model = models.CharField(max_length=100)
    battery_capacity = models.FloatField()
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default="pending")

    request_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"Charging Request by {self.user.username} - Status: {self.status}"
