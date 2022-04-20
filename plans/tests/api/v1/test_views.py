import json

import factory
from django.contrib.auth import get_user_model
from django.test.client import RequestFactory
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import PlanFactory
from plans.models import Plans

fake = Faker()

factory_client = RequestFactory()


class TestTestCase(APITestCase):

    def _create_user_and_login(self, usable_password=True):
        password = "doe" if usable_password else False
        user = self._create_user(password=password)
        self.client.force_login(user)
        # self.client.force_authenticate(user)
        return user

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


class TestPlanListTestCase(TestTestCase):

    def setUp(self) -> None:
        self.url = "/api/v1/plans/?format=json"
        self.plan_data = factory.build(dict, FACTORY_CLASS=PlanFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_valid_data_unauthenticated(self):
        response = self.client.post(self.url, self.plan_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_with_valid_data_succeeds(self):
        # authenticate user
        self._create_user_and_login()

        # create a plan
        response = self.client.post(self.url, self.plan_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        plan = Plans.objects.get(pk=response.data.get('id'))
        self.assertEqual(plan.name, self.plan_data.get('name'))
        self.assertEqual(plan.amount, self.plan_data.get('amount'))
        self.assertEqual(plan.is_active, self.plan_data.get('is_active'))

    def test_put_request_update_with_valid_data_succeeds(self):
        # authenticate user
        self._create_user_and_login()

        # create a plan
        response = self.client.post(self.url, self.plan_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        plan = Plans.objects.get(pk=response.data.get('id'))
        self.assertEqual(plan.name, self.plan_data.get('name'))
        self.assertEqual(plan.amount, self.plan_data.get('amount'))


class TestPlanDetailTestCase(TestTestCase):

    def setUp(self) -> None:
        self.url = "/api/v1/plans/?format=json"
        self.detail_url = "/api/v1/plans/{pk}/?format=json"
        self.plan_data = factory.build(dict, FACTORY_CLASS=PlanFactory)

    def test_get_request_with_failure(self):
        response = self.client.get(self.url, {"pk": 2})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_with_success(self):
        # authenticate user
        self._create_user_and_login()

        # create a plan
        response = self.client.post(self.url, self.plan_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get plan by id
        response = self.client.get(self.url, {"pk": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # convert response data to dict
        response_data = json.loads(json.dumps(response.data))[0]

        plan = Plans.objects.get(pk=response_data['id'])
        self.assertEqual(plan.name, self.plan_data.get('name'))
        self.assertEqual(plan.amount, self.plan_data.get('amount'))
        self.assertEqual(plan.is_active, self.plan_data.get('is_active'))

    def test_put_request_update_with_success(self):
        # authenticate user
        self._create_user_and_login()

        # create a plan
        create_response = self.client.post(self.url, self.plan_data)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        # set payload
        update_payload = {
            'name': 'Boo',
            'amount': create_response.data.get('amount'),
            'is_active': create_response.data.get('is_active'),
            'description': create_response.data.get('description'),
        }

        # update plan by id
        url = self.detail_url.format(pk=create_response.data.get('id'))
        update_response = self.client.patch(url, update_payload, format='json', follow=True)
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

        plan = Plans.objects.get(pk=create_response.data.get('id'))
        self.assertEqual(plan.name, update_payload['name'])


class TestPlanDeleteTestCase(TestTestCase):

    def setUp(self) -> None:
        self.url = "/api/v1/plans/?format=json"
        self.detail_url = "/api/v1/plans/{pk}?format=json"
        self.plan_data = factory.build(dict, FACTORY_CLASS=PlanFactory)

    def test_delete_request_with_failure(self):
        # create a plan
        plan = Plans.objects.create(**self.plan_data)

        # deactivate a plan
        response = self.client.delete(self.url, {'pk': plan.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_delete_request_with_success(self):
    #     # authenticate user
    #     self._create_user_and_login()
    #
    #     # create a plan
    #     plan = Plans.objects.create(**self.plan_data)
    #
    #     # deactivate a plan
    #     url = self.detail_url.format(pk=plan.id)
    #     # response = self.client.delete(url, follow=True)
    #     # response = self.client.delete(self.url, {'pk': plan.id}, format='json', follow=True)
    #     response = self.client.delete(url, format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #
    #     updated_plan = Plans.objects.get(pk=plan.id)
    #     self.assertEqual(updated_plan.is_active, False)
