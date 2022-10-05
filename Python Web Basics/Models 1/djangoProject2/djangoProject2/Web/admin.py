from django.contrib import admin

from djangoProject2.Web.models import Employee, NullBlankDemo


# This model is enabled in Django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'review')
    list_filter = ('first_name')
    search_fields = ('review')

    fieldsets = (
        'personal info',
        {
            'fields':('first_name', 'review')
        }
    )

@admin.register(NullBlankDemo)
class NullBlankDemo(admin.ModelAdmin):
    pass