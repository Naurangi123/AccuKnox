# myapp/views.py
from django.http import HttpResponse
from app.models import SignalModel
from django.shortcuts import render
import time

# Synchronous view 
def sync_signal_view(request):
    print("Before saving the model...")
    instance = SignalModel.objects.create(name="Test Sync Instance")
    print("After saving the model...")

    return HttpResponse("Sync signal triggered")

# Asynchronous view 
def async_signal_view(request):
    print("Before saving the model asynchronously...")
    instance = SignalModel.objects.create(name="Test Async Instance")
    print("After saving the model asynchronously...")

    return HttpResponse("Async signal triggered")
