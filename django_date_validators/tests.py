from datetime import date, datetime, timedelta

from django.test import TestCase
from django_date_validators import validators


class DateIsFutureTestCase(APITestCase):
    """
    """
    def setUp(self):
        self.past_date = date.today() - timedelta(days=1)
        self.present_date = date.today()
        self.future_date = date.today() + timedelta(days=1)

    def test_valid(self):
        self.assertNotEqual(
            validators.date_is_future(self.past_date),
            True
        )
        self.assertNotEqual(
            validators.date_is_future(self.present_date),
            True
        )
        self.assertEqual(
            validators.date_is_future(self.future_date),
            True
        )


class DateIsPresentOrFutureTestCase(APITestCase):
    """
    """
    def setUp(self):
        self.past_date = date.today() - timedelta(days=1)
        self.present_date = date.today()
        self.future_date = date.today() + timedelta(days=1)

    def test_valid(self):
        self.assertNotEqual(
            validators.date_is_future(self.past_date),
            True
        )
        self.assertEqual(
            validators.date_is_future(self.present_date),
            True
        )
        self.assertEqual(
            validators.date_is_future(self.future_date),
            True
        )


class DateIsPresentOrFutureTestCase(APITestCase):
    """
    """
    def setUp(self):
        self.past_date = date.today() - timedelta(days=1)
        self.present_date = date.today()
        self.future_date = date.today() + timedelta(days=1)

    def test_valid(self):
        self.assertNotEqual(
            validators.date_is_present_or_future(self.past_date),
            True
        )
        self.assertEqual(
            validators.date_is_present_or_future(self.present_date),
            True
        )
        self.assertEqual(
            validators.date_is_present_or_future(self.future_date),
            True
        )


class DateIsPastTestCase(APITestCase):
    """
    """
    def setUp(self):
        self.past_date = date.today() - timedelta(days=1)
        self.present_date = date.today()
        self.future_date = date.today() + timedelta(days=1)

    def test_valid(self):
        self.assertEqual(
            validators.date_is_past(self.past_date),
            True
        )
        self.assertNotEqual(
            validators.date_is_past(self.present_date),
            True
        )
        self.assertNotEqual(
            validators.date_is_past(self.future_date),
            True
        )


class DateIsPastOrPresentTestCase(APITestCase):
    """
    """
    def setUp(self):
        self.past_date = date.today() - timedelta(days=1)
        self.present_date = date.today()
        self.future_date = date.today() + timedelta(days=1)

    def test_valid(self):
        self.assertEqual(
            validators.date_is_past_or_present(self.past_date),
            True
        )
        self.assertEqual(
            validators.date_is_past_or_present(self.present_date),
            True
        )
        self.assertNotEqual(
            validators.date_is_past_or_present(self.future_date),
            True
        )
