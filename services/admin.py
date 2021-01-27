from django.contrib import admin
from .models import Service, TimeSlot, Appointement


admin.site.register(Service)
admin.site.register(TimeSlot)
admin.site.register(Appointement)
