from django.forms import ModelForm
from django import forms
from .models import TimeSlot, Service
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


class ServiceSlotsForm(ModelForm):
    class Meta:
        model = TimeSlot
        exclude = ()
        widgets = {
            "date": forms.DateInput(
                format=("%m/%d/%Y"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            'start_time': forms.TimeInput(attrs={'type': 'time'})
        }


SlotFormSet = inlineformset_factory(
    Service, TimeSlot, form=ServiceSlotsForm,
    fields=['date', 'start_time'], extra=1, can_delete=True
)


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        exclude = ['created_by', ]

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('title'),
                Field('desription'),
                Fieldset('Add slots',
                         Formset('slots')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
