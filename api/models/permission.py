from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code_name = models.CharField(max_length=100, unique=True)
    module_name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
