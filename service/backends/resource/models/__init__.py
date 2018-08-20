from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel


# 频道
class Invoice(TimeStampedModel):
    title = models.CharField(verbose_name='标题', max_length=100, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='所属人', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _(u'发票数据')
        verbose_name_plural = _(u'发票数据')


# 商品
class Goods(TimeStampedModel):
    invoice = models.ForeignKey(Invoice, verbose_name='发票', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name='商品名字', max_length=100, default='')
    price = models.FloatField(verbose_name='商品单价', default=0.00)
    quant = models.IntegerField(verbose_name='商品数量', default=0)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = _(u'商品数据')
        verbose_name_plural = _(u'商品数据')

