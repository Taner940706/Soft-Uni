from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    lastname = models.CharField(
        max_length=30,
    )

    age = models.PositiveIntegerField()
