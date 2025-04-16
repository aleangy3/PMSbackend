from django.db import models


class Logs(models.Model):
    text = models.TextField()

    created_by = models.ForeignKey("User", on_delete=models.CASCADE, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by.name} {self.created_at}"
