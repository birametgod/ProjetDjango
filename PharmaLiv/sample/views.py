from django.views.generic import FormView
from patient.models import Patient
from pharmacie.models import Pharmacie
from sample.forms import SampleForm
from django.shortcuts import render, redirect


class SampleFormView(FormView):
    template_name = "sample/index.html"
    form_class = SampleForm

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(SampleFormView, self).get_context_data(**kwargs)
        context = {
            'pharmacie': Pharmacie.objects.all(),
            'form':SampleForm,
        }
        return context
