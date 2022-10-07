from django.contrib import admin

from djangoProject2.Web.models import Employee, NullBlankDemo


# This model is enabled in Django admin

@admin.register(NullBlankDemo)
class NullBlankDemo(admin.ModelAdmin):
    pass