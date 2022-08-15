from django import forms
from django.utils.translation import gettext_lazy as _
from main.forms.GenericForm import GenericForm
from main.models import Event


class EventForm(GenericForm):
    class Meta:
        model = Event
        fields = ["time", "year", "label", "source"]
        labels = {
            "time": _("Historic time (hh:mm)"),
            "year": _("Year of the event"),
            "label": _("A short sentence describing the event"),
            "source": _("A link where people can read more about it"),
        }
    
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['year'].required = False
        self.fields['year'].widget.attrs["placeholder"] = _("Not required")
        self.fields["time"].widget = forms.TimeInput(format='%H:%M')
