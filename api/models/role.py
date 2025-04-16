from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code_name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField("Permission", related_name="+")

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        "User", related_name="+", blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
