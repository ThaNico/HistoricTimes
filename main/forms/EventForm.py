from django import forms
from django.utils.translation import gettext_lazy as _
from main.forms.GenericForm import GenericForm
from main.models import Event


class EventForm(GenericForm):
    class Meta:
        model = Event
        fields = ["time", "label", "source"]
        labels = {
            "time": _("Historic time"),
            "label": _("A short sentence describing the event and when it happened"),
            "source": _("A link where people can read more about it"),
        }
    
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["time"].widget = forms.TimeInput(format='%H:%M')
        self.fields["time"].widget.attrs["placeholder"] = _("Required format: hh:mm")
        self.fields["label"].widget.attrs["placeholder"] = _("Maximum 128 characters")
        self.fields["source"].widget.attrs["placeholder"] = _("Use a well known https source")
