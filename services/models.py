from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
CustomUser = get_user_model()


class Service(models.Model):
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='services'
    )
    title = models.CharField(max_length=100)
    desription = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class TimeSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, related_name="slots"
    )

    def __str__(self):
        return str(self.date)
