from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

INVOICE_CHOICES = (
    ('办公用品', '办公用品'),
    ('出差报销', '出差报销'),
    ('工资避税', '工资避税'),
)


# 部门
class Department(models.Model):
    title = models.CharField(verbose_name='部门名称', max_length=100, default='')
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _(u'公司部门')
        verbose_name_plural = _(u'公司部门')


class Invoice(TimeStampedModel):
    title = models.CharField(verbose_name='发票类型', max_length=100, choices=INVOICE_CHOICES)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='所属人', on_delete=models.CASCADE, blank=True,
                              null=True)
    total = models.DecimalField(verbose_name='总计', max_digits=10, decimal_places=2, default=0.00)
    remark = models.TextField(verbose_name='备注', blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name='公司部门', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _(u'发票数据')
        verbose_name_plural = _(u'发票数据')


# 商品
class Goods(TimeStampedModel):
    invoice = models.ForeignKey(Invoice, verbose_name='发票', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name='商品名字', max_length=100, default='')
    total = models.DecimalField(verbose_name='商品小计', max_digits=10, decimal_places=2, default=0.00)
    price = models.DecimalField(verbose_name='商品单价', max_digits=10, decimal_places=2, default=0.00)
    quant = models.IntegerField(verbose_name='商品数量', default=1)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.total = self.price * self.quant
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'商品数据')
        verbose_name_plural = _(u'商品数据')
