from django.urls import path, include
from .views import *

urlpatterns = [
    path("", ListServices.as_view(), name="list_services"),
    path("<int:pk>/slots", ListSlots.as_view(), name="list_slots"),
    path("services/", CreateServices.as_view(), name='create-service'),
    path("services/<int:pk>", ServiceDetail.as_view(), name="service_detail")

]
