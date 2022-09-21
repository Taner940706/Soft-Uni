from django.db import models

# Create your models here.

# Maps to a db table


class Task(models.Model):
    # varchar (30) not null
    name = models.CharField(
        max_length=30,
        null=False,
    )

    description = models.TextField()
    priority = models.IntegerField()