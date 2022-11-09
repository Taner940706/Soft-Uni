from django.contrib.auth import models as auth_models
from django.db import models


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    # here we set our email address as username
    # because in the AbstractBaseUser we have only password by default
    USERNAME_FIELD = 'email'


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25
    )
    last_name = models.CharField(
        max_length=25
    )
    age = models.PositiveIntegerField()
    user = models.OneToOneField(
        auth_models.User,
        primary_key=True,
        on_delete=models.CASCADE,
    )
