from rest_framework import serializers
from .models import Appointement
from services.models import Service, TimeSlot


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointement
        fields = "__all__"

        def create(self, request):
            current_user = self.context['request'].user
            body = self.context["request"].data
            slot_id = body["id"]
            selected_slot = TimeSlot.objects.get(id=slot_id)
            instance = Appointement.objects.create(
                selected_slot=selected_slot, customer=current_user)

            instance.save()
            return instance
