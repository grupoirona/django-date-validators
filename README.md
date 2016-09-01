# django-date-validators

Simple but useful validators for django.db.models.DateField and django.db.models.DateTimeField.

## Quick start

1. Install it through pip:

    pip3 install django-date-validators


2. Include to your INSTALLED_APPS setting:

    INSTALLED_APPS = [
        ...
        'django_date_validators',
    ]


3. Just add it to your models:

    from django.db import models
    from django_date_validators.validators import date_is_present_or_future

    class Example(models.Model):
        """
        """
        due_date = models.DateField(
            validators=[date_is_present_or_future]
        )

4. That's it!
