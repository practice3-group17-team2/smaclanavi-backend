"""
テストしたいserializerはClassInfo, Review, 
UpcomingLecInfo, LecScheduel の4つ
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from .. import serializers
from .. import models
from .. import views

# Create your tests here.

# Run test with below command
# manage.py test administer_data.tests.test_views


class TestClassInfoSerializer(TestCase):
    serializer = serializers.ClassInfoSerializer
    factory = APIRequestFactory()


    # def test_create_account(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     url = reverse('account-list')
    #     data = {'name': 'DabApps'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Account.objects.count(), 1)
    #     self.assertEqual(Account.objects.get().name, 'DabApps')
    
    def test_list(self):
        url = reverse("class_info-list")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["class_name"], "あいうえお")
        self.assertEqual(response.data[1]["city"]["city_name"], "赤羽")

    def test_create(self):
        url = reverse("class_info-list")
        data = {
            "class_name": "皇居",
            "organizer": {
                "org_id": 1
            },
            "city": {
                "city_id": 1
            },
            "lecture": [{
                "lec_id": 1
            }, {
                "lec_id": 2
            }],
            "phone_number": "",
            "address": "",
            "evaluation": 0,
            "price": 0,
            "site_url": "",
            "has_parking": False,
            "is_barrier_free": False
        }
        post_response = self.client.post(url, data, format="")
        # print(post_response.data)

        request = self.factory.get("/class_infos/")
        view = views.ClassInfoViewSet.as_view({'get': 'list'})
        get_response = view(request)

        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(len(get_response.data), 3)
        self.assertEqual(get_response.data[2]["class_name"], "皇居")
        self.assertEqual(get_response.data[1]["city"]["city_name"], "赤羽")

    def test_retrieve(self):
        instance_id = "d1013537a8694d1ca444513f6d3be5d9"
        request = self.factory.get("/class_infos/"+instance_id, pk=instance_id)
        view = views.ClassInfoViewSet.as_view({'get': 'retrieve'})
        response = view(request)
        print(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["class_name"], "あいうえお")
        self.assertEqual(response.data[1]["city"]["city_name"], "赤羽")


    def test_detail_put(self):
        pass

    def test_detail_delete(self):
        pass


class TestReviewSerializer(TestCase):
    pass


class TestUpcomingLecInfoSerializer(TestCase):
    pass


class TestLecScheduleSerializer(TestCase):
    pass