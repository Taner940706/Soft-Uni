from django.db.models import signals
from django.dispatch import receiver

from common_web_tools.web.models import Employee


@receiver(signals.post_save, sender = Employee)
def handle_employee_created(*args, **kwargs):
    print(args)
    print(kwargs)