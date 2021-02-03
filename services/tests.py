from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
import json
from .models import Service


class ServicesTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.owner = User.objects.create_user(
            username="abdullah", email="abdullah@email.com", password="testpass123"
        )

    def test_create_service(self):
        self.client.force_login(self.owner)
        response = self.client.post(reverse(
            'create-service'), date={"title": 'title1', "desription": "desription1"})
        self.assertEqual(response.status_code, 200)
        print("run", Service.objects.all())
        self.assertEqual(Service.objects.all().last().title, "title1")
