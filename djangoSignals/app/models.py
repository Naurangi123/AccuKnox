import asyncio
import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
from asgiref.sync import async_to_sync

class SignalModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=SignalModel)
def my_model_post_save_handler(sender, instance, created, **kwargs):
    print("Signal received, starting handler...")
    print(f"Signal handler running in thread: {threading.current_thread().name}")
    time.sleep(2)  #synchronous

@receiver(post_save, sender=SignalModel)
def my_model_post_save_handler_async(sender, instance, created, **kwargs):
    async def async_task():
        print("Signal received, starting handler asynchronously...")
        print(f"Before saving, in thread: {threading.current_thread().name}")
        await asyncio.sleep(2) #non-blocking
        print(f"Handler finished processing: {instance.name}")
        print(f"After saving, in thread: {threading.current_thread().name}")

    async_to_sync(async_task)() 
