from datetime import datetime
from django.http import JsonResponse
from django.views import View
from main.models import Event

MAX_EVENTS_PER_LOAD = 20


class EventsView(View):
    def get(self, request, hours, minutes):
        time = datetime.strptime(hours + ':' + minutes, '%H:%M').time()
        results = Event.objects.filter(status=Event.Status.VALID, time=time)[:MAX_EVENTS_PER_LOAD]
        print("found results for time : " + str(time))
        print(results)
        
        return JsonResponse({})
