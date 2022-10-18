from django.db import models

from djangoProject3.web.validate import validate_text, ValidationRange


class Todo(models.Model):
    MAX_LEN_TEXT = 25
    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        validators=(validate_text,),
        blank=False,
        null=False,
    )

    priority = models.IntegerField(
        validators=(ValidationRange(1, 10),),
        blank=False,
        null=False,
    )
    is_done = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )
