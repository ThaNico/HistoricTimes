from datetime import datetime
from django.http import JsonResponse
from django.views import View
from main.models import Event
from ..moserializers import EventSerializer
from itertools import groupby


class EventsView(View):
    # We load the current hour and the client will cache it
    # One nice way would have been to retrieve N results from each HH:MM, kinda like sampling
    # But I think it might slow down everything so I'll need to benchmark later with more data
    def get(self, request, hours):
        timeStart = datetime.strptime(str(hours) + ':00', '%H:%M').time()
        timeEnd = datetime.strptime(str(hours) + ':59', '%H:%M').time()
        
        results = Event.objects.filter(status=Event.Status.VALID, time__gte=timeStart, time__lte=timeEnd)\
            .values("label", "source", "time").order_by('time')
        jsonData = EventSerializer(results, many=True).data

        # This should be done via sql but I had troubles with the orm .annotate
        groups = groupby(jsonData, lambda content: content['time'])
        dic = {}
        for k, v in groups:
            dic[k] = list(v)

        return JsonResponse(dic, safe=False)
