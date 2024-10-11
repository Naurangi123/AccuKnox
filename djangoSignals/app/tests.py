
from django.test import TestCase
from django.db import transaction
from .models import SignalModel

class SignalModelTest(TestCase):

    def test_signal_transaction_behavior(self):
        print("Starting test for signal transaction behavior")
        
        with transaction.atomic():
            instance = SignalModel.objects.create(name="test instance")
            print("Model instance created. Check signal output.")
class SignalModelOnCommitTest(TestCase):

    def test_signal_on_commit(self):
        print("Starting test for signal on commit")

        def on_commit_signal_action():
            print("Signal executed within the same transaction after commit!")

        with transaction.atomic():
            transaction.on_commit(on_commit_signal_action)
            instance = SignalModel.objects.create(name="test instance on commit")
            print("Model instance created. Signal will execute on commit.")

