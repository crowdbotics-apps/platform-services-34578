
from django.urls import reverse
from rest_framework import status
# from nose.tools import ok_, eq_
# from django.test import TestCase
from rest_framework.test import APITestCase
import factory
from .models import Plans
from .tests.factories import PlanFactory

# Create your tests here.


class TestPlanListTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('plans')
        self.plan_data = factory.build(dict, FACTORY_CLASS=PlanFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, "status.HTTP_400_BAD_REQUEST")
