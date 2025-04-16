from django.db import models


class Payment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=[("pending", "Pending"), ("completed", "Completed")]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.DO_NOTHING
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"Payment by {self.user.username} - Status: {self.status}"
