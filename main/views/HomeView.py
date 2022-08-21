from django.shortcuts import render
from django.views import View
from historic_times.utils import requestUtil


class HomeView(View):
    def get(self, request):
        templateContext = {}
        requestUtil.moveSessionMessageToContext(requestUtil.KEY_REQUEST_MSG_SUCCESS, request, templateContext)
        return render(request, "home.html", templateContext)
