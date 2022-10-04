from django.contrib import admin

from djangoProject2.Web.models import Employee


# This model is enabled in Django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass