
from django.urls import path
from .views import sync_signal_view, async_signal_view

urlpatterns = [
    path('sync/', sync_signal_view, name='sync_signal'),
    path('async/', async_signal_view, name='async_signal'),
]
