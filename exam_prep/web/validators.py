from django.core import exceptions


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and '_' not in value:
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")
