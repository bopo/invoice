from django.dispatch import receiver

from . import signals


@receiver(signals.my_signal, dispatch_uid="my_signal_receiver")
def my_signal_handler(sender, **kwargs):
    print('my_signal received')


@receiver(signals.push_signal, dispatch_uid="push_signal_receiver")
def push_signal_handler(sender, **kwargs):
    print('my_signal received')


@receiver(signals.sms_signal, dispatch_uid="sms_signal_receiver")
def sms_signal_handler(sender, **kwargs):
    print('my_signal received')
