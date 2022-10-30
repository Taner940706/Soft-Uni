from django.core import exceptions


def validate_between_years(value):
    if 2049 < value < 1980:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")


def validate_min_len_username(value):
    if len(value) < 2:
        raise exceptions.ValidationError("The username must be a minimum of 2 chars")