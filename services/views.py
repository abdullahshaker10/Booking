from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Service
from .forms import *
from django.db import transaction
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class ListServices(ListView):
    context_object_name = "services"
    queryset = Service.objects.all()
    template_name = "services/services_list.html"
    paginate_by = 10


class ListSlots(ListView):
    context_object_name = "slots"
    template_name = "services/slots_list.html"

    def get_queryset(self, *args,  **kwargs):
        service_id = self.kwargs['pk']
        service = Service.objects.get(id=service_id)
        return service.slots.all()



class ServiceDetail(DetailView):
    model = Service
    template_name = "services/service_detail.html"


class CreateServices(LoginRequiredMixin, CreateView):
    form_class = ServiceForm
    template_name = "services/services_form.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        data = super(CreateServices, self).get_context_data(**kwargs)
        if self.request.POST:
            data['slots'] = SlotFormSet(self.request.POST)
        else:
            data['slots'] = SlotFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        slots = context['slots']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if slots.is_valid():
                slots.instance = self.object
                slots.save()
        return super(CreateServices, self).form_valid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        slots = context['slots']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if slots.is_valid():
                slots.instance = self.object
                slots.save()
        return super(CreateServices, self).form_valid(form)

    def get_success_url(self):
        return reverse('service_detail', kwargs={'pk': self.object.pk})
