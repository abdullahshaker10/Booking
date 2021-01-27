from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=1500, null=True, blank=True)