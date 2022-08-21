from django.urls import path

from main.views.HomeView import HomeView

from .views.EventsAddView import EventsAddView
from .views.EventsView import EventsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/<int:hours>', EventsView.as_view(), name='events'),
    path('add-event', EventsAddView.as_view(), name='add-event'),
]
