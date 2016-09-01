===============
Date Validators
===============

Django Date Validators is a simple way to validate your
django.db.models.DateField and django.db.models.DateTimeField model fields.


Quick start
-----------

1. Install it with pip::

    pip3 install django-date-validators

2. Add it to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_date_validators',
    ]

3. Include them in your models like this::

    from django.db import models
    from django_date_validators.validators import date_is_present_or_future

    due_date = models.DateField(
        validators=[date_is_present_or_future]
    )

4. That's it!
