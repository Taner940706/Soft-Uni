from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_text(value):
    if '_' in value:
        raise ValidationError(message="_ is a invalid symbol",
                              code='invalid',)


def validate_priority(value):
    if value < 1 or value > 10:
        raise ValidationError("Only numbers between 1 to 10")


@deconstructible
class ValidationRange:
    def __init__(self, min_value, max_value):
        self.max_value = max_value
        self.min_value = min_value

    def __call__(self, value):
        if value < 1 or value > 10:
            raise ValidationError(f"Only numbers between {self.min_value} to {self.max_value}")

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.min_value == other.min_value
            and self.max_value == other.max_value
        )


