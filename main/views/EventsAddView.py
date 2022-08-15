from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class EventsAddView(View):
    def get(self, request):
        return render(request, "events-add.html")

    def post(self, request):
        print("add")
        return JsonResponse({})
