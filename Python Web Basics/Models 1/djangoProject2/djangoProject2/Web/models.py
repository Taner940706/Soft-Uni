from django.db import models

# Create your models here.


class Employee(models.Model):
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


#Employee.objects.all() # select
#Employee.objects.create() #insert
#Employee.objects.filter() #select + where
#Employee.objects.update() #update


def __str__(self):
    return f"Name: {self.first_name}"