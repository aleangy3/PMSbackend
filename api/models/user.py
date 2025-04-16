import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


def get_profile_image_path(self, filename):
    return f"profile_images/users/{self.pk}/{str(uuid.uuid4())}.png"


def get_default_profile_image_path():
    return f'profile_images/{"default_profile_image.png"}'


class UserManager(BaseUserManager):
    def create_user(self, id, username, email, password=None):
        if not username:
            raise ValueError("User must have a username.")
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(
            id=id,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, username, email, password):
        user = self.create_user(id=id, username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)  # For phone numbers
    profile_status = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(
        max_length=255,
        upload_to=get_profile_image_path,
        null=True,
        blank=True,
        default=get_default_profile_image_path,
    )
    role = models.ForeignKey(
        "Role", related_name="users", blank=True, null=True, on_delete=models.CASCADE
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]  # Required for createsuperuser command

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser