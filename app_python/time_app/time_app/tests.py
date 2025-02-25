from django.test import TestCase
from django.urls import reverse
from datetime import datetime
import pytz
import re


class MoscowTimeViewTests(TestCase):
    """
    Test case for the Moscow time view.
    """

    def test_moscow_time_view_status_code(self):
        """
        Test if the Moscow time view returns a 200 status code.
        """
        response = self.client.get(reverse('moscow_time'))
        self.assertEqual(response.status_code, 200)

    def test_moscow_time_view_content(self):
        """
        Test if the response contains the correct Moscow time format.
        """
        response = self.client.get(reverse('moscow_time'))
        match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", response.content.decode())
        self.assertIsNotNone(match, "Response does not contain a valid timestamp")

    def test_moscow_time_correctness(self):
        """
        Test if the time displayed is close to the actual Moscow time.
        """
        response = self.client.get(reverse('moscow_time'))
        match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", response.content.decode())
        self.assertIsNotNone(match, "Response does not contain a valid timestamp")
        response_time_str = match.group(1)
        response_time = datetime.strptime(response_time_str, "%Y-%m-%d %H:%M:%S")
        moscow_timezone = pytz.timezone("Europe/Moscow")
        actual_moscow_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
        actual_moscow_time_obj = datetime.strptime(actual_moscow_time, "%Y-%m-%d %H:%M:%S")
        time_difference = abs((actual_moscow_time_obj - response_time).total_seconds())
        self.assertLessEqual(time_difference, 5, "Moscow time in response is incorrect")
