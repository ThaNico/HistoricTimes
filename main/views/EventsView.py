from datetime import datetime
from django.http import JsonResponse
from django.views import View
from main.models import HistoricHour


class EventsView(View):
    def get(self, request, hours, minutes):
        time = datetime.strptime(hours + ':' + minutes, '%H:%M').time()
        results = HistoricHour.objects.filter(status=HistoricHour.Status.VALID, time=time)
        print("found results for time : " + str(time))
        print(results)
        
        return JsonResponse({})
