from typing import Any, Type

from django.db import transaction
from django.forms.models import BaseInlineFormSet, BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import EntryFormSet, PlayerDemographyForm
from .models import Entry, PlayerDemography

# Create your views here.


class ReportView(CreateView):
    template_name = "add_report.html"
    success_url = "/report/add/"
    form_class = PlayerDemographyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = EntryFormSet(self.request.POST, self.request.FILES, instance=self.object)

        else:
            context["formset"] = EntryFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formsets = context["formset"]
        with transaction.atomic():
            self.object = form.save()
            if formsets.is_valid():
                formsets.instance = self.object
                formsets.save()
            else:
                return self.form_invalid(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
