from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        print("yes")
        return render(request, "home.html", {})
