from typing import Any
from django.forms.models import BaseModelForm, BaseInlineFormSet
from django.http import HttpRequest, HttpResponse
from django.db import transaction
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import PlayerDemographyForm, EntryFormSet
from typing import Type
# Create your views here.
class ReportView(CreateView):
    template_name = 'add_report.html'
    success_url = '/report/add/'
    form_class = PlayerDemographyForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = EntryFormSet()
        return context
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        formset = EntryFormSet(self.request.POST, self.request.FILES)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form: BaseModelForm, formset:Type[BaseInlineFormSet]) -> HttpResponse:
        with transaction.atomic():
            objects = form.save()
            for forms in formset:
                forms.instance.player_id = objects
                forms.save()
        return super().form_valid(form)

