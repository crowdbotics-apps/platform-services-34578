import json
from datetime import datetime

import factory
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.test.client import RequestFactory
from django.http import JsonResponse
from django.utils.timezone import make_aware
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from subscriptions.models import Subscriptions
from .factories import PlanFactory
from plans.models import Plans

fake = Faker()

factory_client = RequestFactory()


class TestTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = "/api/v1/subscriptions/?format=json"
        self.plan_data = factory.build(dict, FACTORY_CLASS=PlanFactory)

    def _create_user(self, username="john", password="doe", **kwargs):
        user = get_user_model().objects.create(
            username=username, is_active=True, **kwargs
        )
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def _create_user_and_login(self, usable_password=True):
        password = "doe" if usable_password else False
        user = self._create_user(password=password)
        self.client.force_login(user)  # self.client.force_authenticate(user)
        return user

    def _create_plan(self):
        self.plan = Plans.objects.create(**self.plan_data)
        return self.plan

    def _login_and_create_subscription(self):
        # authenticate user
        user = self._create_user_and_login()

        # create a plan
        plan = self._create_plan()

        # create a subscription
        start_at = make_aware(datetime.now())
        end_at = start_at + relativedelta(months=1)
        subscription_payload = {
            "start_at": start_at,
            "end_at": end_at,
            "user": user,
            "plan": plan,
            "is_active": True,
        }
        return Subscriptions.objects.create(**subscription_payload)


class TestSubscriptionListTestCase(TestTestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_get_request_unauthenticated(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_authenticated_succeeds(self):
        # authenticate and create subscription
        self._login_and_create_subscription()

        # get subscription
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestSubscriptionCreateTestCase(TestTestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_post_request_with_no_data_fails(self):
        # create a plan
        plan = self._create_plan()
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_valid_data_unauthenticated(self):
        # create a plan
        plan = self._create_plan()

        response = self.client.post(self.url, {'plan': plan.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_with_valid_data_succeeds(self):
        # authenticate user
        user = self._create_user_and_login()

        # create a plan
        plan = self._create_plan()

        # create a subscription
        payload_data = {'plan': plan.id, 'max_apps': 2}
        response = self.client.post(self.url, payload_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        subscription = Subscriptions.objects.get(pk=response.data.get('id'))
        self.assertEqual(subscription.user, user)
        self.assertEqual(subscription.plan, plan)
        self.assertEqual(subscription.is_active, True)


class TestSubscriptionUpdateTestCase(TestTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.detail_url = "/api/v1/subscriptions/{pk}/?format=json"

    def test_post_request_with_no_data_fails(self):
        # create a plan
        self._create_plan()
        response = self.client.patch(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_valid_data_unauthenticated(self):
        subscription = self._login_and_create_subscription()
        self.client.logout()

        url = self.detail_url.format(pk=subscription.id)
        response = self.client.put(url, {'plan': subscription.plan_id, 'is_active': False}, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_with_valid_data_succeeds(self):
        subscription = self._login_and_create_subscription()

        url = self.detail_url.format(pk=subscription.id)
        response = self.client.put(url, {'plan': subscription.plan_id, 'is_active': False}, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('is_active'), False)