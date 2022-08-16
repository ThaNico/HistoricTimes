from datetime import datetime
from django.http import JsonResponse
from django.views import View
from main.models import Event
from ..moserializers import EventSerializer
from django.utils.translation import gettext_lazy as _

MAX_EVENTS_PER_LOAD = 20


class EventsView(View):
    def get(self, request, hours, minutes):
        time = datetime.strptime(hours + ':' + minutes, '%H:%M').time()
        
        results = Event.objects.filter(status=Event.Status.VALID, time=time)\
            .values("label", "source").order_by('-id')[:MAX_EVENTS_PER_LOAD]
        jsonData = EventSerializer(results, many=True).data if results else {"message" : _("There are no events to display at this time.")}
        return JsonResponse(jsonData, safe=False)
