from django.shortcuts import render
from django.views import View
from historic_hours.utils import requestUtil


class HomeView(View):
    def get(self, request):
        templateContext = {}
        requestUtil.moveSessionMessageToContext("message_success", request, templateContext)
        return render(request, "home.html", templateContext)
