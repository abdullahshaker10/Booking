from django.db import models
from django.contrib.auth import get_user_model
from services.models import Service, TimeSlot
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail

CustomUser = get_user_model()


class Appointement(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointemts'
    )
    selected_slot = models.OneToOneField(
        TimeSlot, on_delete=models.CASCADE, null=True, blank=True)
