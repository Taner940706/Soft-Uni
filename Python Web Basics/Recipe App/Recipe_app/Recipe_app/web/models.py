from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LEN = 30
    INGREDIENT_MAX_LEN = 250
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    image_url = models.ImageField()
    description = models.TextField()
    ingredients = models.CharField(
        max_length=INGREDIENT_MAX_LEN,
    )
    time = models.IntegerField()

