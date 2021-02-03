from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Appointement
from services.models import TimeSlot
from .serializers import AppointmentSerializer


class CreateAppointment(CreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointement.objects.all()

    def post(self, request, *args, **kwargs):
        body = request.data
        slot_id = body["id"]
        request.data["customer"] = request.user.id
        request.data["selected_slot"] = slot_id
        return self.create(request, *args, **kwargs)
