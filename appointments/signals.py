from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointement
from django.conf import settings
from django.core.mail import send_mail
