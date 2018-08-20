import django.dispatch

my_signal = django.dispatch.Signal(providing_args=["my_signal_arg1", "my_signal_arg_2"])

push_signal = django.dispatch.Signal(providing_args=["receiver", "message", 'extra'])

sms_signal = django.dispatch.Signal(providing_args=["receiver", "message", 'extra'])
