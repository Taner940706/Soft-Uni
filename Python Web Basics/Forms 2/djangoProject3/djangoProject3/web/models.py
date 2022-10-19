from django.core.exceptions import ValidationError
from django.db import models

from djangoProject3.web.validate import validate_text, ValidationRange


class Person(models.Model):
    MAX_LEN_NAME = 20
    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )
    profile_img = models.ImageField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_TODOS_COUNT_PER_PERSON = 3
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

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )

    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        if assignee.todo_set.count() > Todo.MAX_TODOS_COUNT_PER_PERSON:
            raise ValidationError(f'{assignee} is already assigned max todos!')
        return assignee
