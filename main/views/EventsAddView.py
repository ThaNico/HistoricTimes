from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from historic_times.utils import requestUtil

from ..forms.EventForm import EventForm


class EventsAddView(View):
    template_name = "events-add.html"
    form_class = EventForm

    def get(self, request):
        templateContext = {"form": self.form_class()}
        return render(request, self.template_name, templateContext)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid() and requestUtil.isCaptchaValid(request.POST["h-captcha-response"]):
            form.save()
            requestUtil.addMessageSuccess(request.session, str(_("Thank you, the event will be reviewed by moderators !")))
            return redirect("home")
        
        templateContext = {"form": form}
        requestUtil.addMessageError(templateContext, str(_("An error occured, please check your data or try again later.")))
        return render(request, self.template_name, templateContext)
