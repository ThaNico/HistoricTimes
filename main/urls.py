from django.urls import path
from .views.EventsView import EventsView

from main.views.HomeView import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/<str:hours>/<str:minutes>', EventsView.as_view(), name='events'),
]
