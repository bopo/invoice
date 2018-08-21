from django.dispatch import receiver

from . import signals


# @receiver(post_save, sender=Invoice)
# def invoice_post_save(instance, created, **kwargs):
#     instance.total = Goods.objects.filter(invoice_id=instance.pk).aggregate(Sum('total')).get('total__sum')
#     instance.total = 0.00 if instance.total is None else instance.total
#     instance.save()


@receiver(signals.my_signal, dispatch_uid="my_signal_receiver")
def my_signal_handler(sender, **kwargs):
    print('my_signal received')


@receiver(signals.push_signal, dispatch_uid="push_signal_receiver")
def push_signal_handler(sender, **kwargs):
    print('my_signal received')


@receiver(signals.sms_signal, dispatch_uid="sms_signal_receiver")
def sms_signal_handler(sender, **kwargs):
    print('my_signal received')
