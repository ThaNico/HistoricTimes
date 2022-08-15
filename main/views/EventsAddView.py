from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from ..forms.EventForm import EventForm


class EventsAddView(View):
    template_name = "events-add.html"
    form_class = EventForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print("add")
            return JsonResponse({})
        return render(request, self.template_name, { 'form': form })
