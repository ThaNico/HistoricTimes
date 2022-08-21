from django.urls import path

from .views.EventsAddView import EventsAddView
from .views.EventsView import EventsView

from main.views.HomeView import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/<int:hours>', EventsView.as_view(), name='events'),
    path('add-event', EventsAddView.as_view(), name='add-event'),
]
