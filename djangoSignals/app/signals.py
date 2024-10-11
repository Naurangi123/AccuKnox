
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from asgiref.sync import async_to_sync
from .models import SignalModel
import asyncio
import time

@receiver(post_save, sender=SignalModel)
def signal_model_post_save_handler_sync(sender, instance, created, **kwargs):
    print("Signal received, starting handler...")
    time.sleep(2)#sleep for 2 seconds
    print(f"Handler finished processing: {instance.name}")


@receiver(post_save, sender=SignalModel)
def signal_model_post_save_handler_async(sender, instance, created, **kwargs):
    async def async_task():
        print("Signal received, starting handler asynchronously...")
        await asyncio.sleep(2) #here code is non-blocking
        print(f"Handler finished processing: {instance.name}")

    async_to_sync(async_task)()

@receiver(post_save, sender=SignalModel)
def signal_model_post_save(sender, instance, **kwargs):
    print("Signal executed!")
    
    if transaction.get_connection().in_atomic_block:
        print("In the same transaction block!")
    else:
        print("Not in the same transaction block!")
