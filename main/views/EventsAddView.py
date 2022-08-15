from django.shortcuts import redirect, render
from django.views import View
from django.utils.translation import gettext_lazy as _

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
            form.save()
            request.session['message_success'] = str(_("Thank you, the event will be reviewed by moderators !"))
            return redirect("home")
        return render(request, self.template_name, { 'form': form })
