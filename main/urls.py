from django.urls import path

from main.views.HomeView import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
