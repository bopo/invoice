INSTALLED_APPS += (
    'service.backends.payments',
    # 'payments', 
)

PAYMENT_HOST = 'localhost:8000'
PAYMENT_USES_SSL = False
PAYMENT_MODEL = 'payments.Payment'
PAYMENT_VARIANTS = {
    'paypal': ('service.payments.provider.paypal.PaypalProvider', {
    	'client_id':'client_id',
    	'secret':'secret', 
    }),
    'dummy': ('service.payments.provider.dummy.DummyProvider', {}),
}
