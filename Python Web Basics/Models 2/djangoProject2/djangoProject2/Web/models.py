from django.db import models
from django.urls import reverse


# Create your models here.


class AuditInfo(models.Model):
    # make class abstract
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,  # optional
    )

    updated_on = models.DateTimeField(
        auto_now=True  # optionas
    )

#inheriting abstract class AuditInfo
class Department(AuditInfo,models.Model):
    name = models.CharField(max_length=15)

    slug = models.SlugField(
        unique=True,
        null = True,
    )

    def get_absolute_url(self):
        url = reverse('details_department', kwargs={
            'pk': self.pk}
                )
        return url

class Employee(models.Model):

    class Meta:
        ordering = ("years_of_experience", "first_name",)

    #var char (30) => strings with max length 30
    first_name = models.CharField(max_length=30)

    #int >0
    years_of_experience = models.PositiveIntegerField()

    # text => strings with unlimited length
    review = models.TextField()

    star_date = models.DateField()

    # this will be automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True, # optional
    )

    updated_on = models.DateTimeField(
        auto_now=True #optionas
    )
    age = models.IntegerField(
        default=-1,
        verbose_name='Age of student'
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )



class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null = False,
    )
    null = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null = models.IntegerField(
        blank=True, #form validation
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )


#Employee.objects.all() # select
#Employee.objects.create() #insert
#Employee.objects.filter() #select + where
#Employee.objects.update() #update


def __str__(self):
    return f"Name: {self.first_name}"