from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from unit_and_integration_testing.web.validators import egn_validator


class Profile(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=(
        MinValueValidator(0),
        MaxValueValidator(150)
    ))
    egn = models.CharField(max_length=10, validators=[egn_validator])
