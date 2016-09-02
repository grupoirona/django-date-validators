from datetime import date, datetime, timedelta

from django.test import TestCase
from django_date_validators import validators


class DateIsFutureTestCase(TestCase):
    """
    """
    def test_valid(self):
        past_date = date.today() - timedelta(days=1)
        present_date = date.today()
        future_date = date.today() + timedelta(days=1)
        self.assertIs(
            validators.date_is_future(past_date),
            False
        )
        self.assertIs(
            validators.date_is_future(present_date),
            False
        )
        self.assertIs(
            validators.date_is_future(future_date),
            True
        )


class DateIsPresentOrFutureTestCase(TestCase):
    """
    """
    def test_valid(self):
        past_date = date.today() - timedelta(days=1)
        present_date = date.today()
        future_date = date.today() + timedelta(days=1)
        self.assertIs(
            validators.date_is_present_or_future(past_date),
            False
        )
        self.assertIs(
            validators.date_is_present_or_future(present_date),
            True
        )
        self.assertIs(
            validators.date_is_present_or_future(future_date),
            True
        )


class DateIsPastTestCase(TestCase):
    """
    """
    def test_valid(self):
        past_date = date.today() - timedelta(days=1)
        present_date = date.today()
        future_date = date.today() + timedelta(days=1)
        self.assertIs(
            validators.date_is_past(past_date),
            True
        )
        self.assertIs(
            validators.date_is_past(present_date),
            False
        )
        self.assertIs(
            validators.date_is_past(future_date),
            True
        )


class DateIsPastOrPresentTestCase(TestCase):
    """
    """
    def test_valid(self):
        past_date = date.today() - timedelta(days=1)
        present_date = date.today()
        future_date = date.today() + timedelta(days=1)
        self.assertIs(
            validators.date_is_past_or_present(past_date),
            True
        )
        self.assertIs(
            validators.date_is_past_or_present(present_date),
            True
        )
        self.assertIs(
            validators.date_is_past_or_present(future_date),
            False
        )
