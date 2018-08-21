import os
from io import StringIO

import xlwt
from django.http import HttpResponse
from django.shortcuts import render

from ..backends.resource.models import Invoice


def report(request):
    ids = request.GET.get('ids', None)
    return render(request, 'report.html', locals())


def excel(request, id=None):
    activitys = Invoice.objects.all().order_by('id')

    if activitys:

        ws = xlwt.Workbook(encoding='utf-8')
        w = ws.add_sheet(u'评论完成', cell_overwrite_ok=True)
        w.write(0, 0, u"订单编号")
        w.write(0, 1, u"买家")
        w.write(0, 2, u"购买时间")
        w.write(0, 3, u"付款金额")
        w.write(0, 4, u"提交订单号")
        w.write(0, 5, u"返现金额")
        w.write(0, 6, u"状态")

        excel_row = 1

        for activity in activitys:
            id = activity.id
            buyer = activity.buyer.buyer.username
            time = activity.time
            price = activity.pay
            orderId = activity.orderId
            payBack = activity.payBack
            status = activity.status

            w.write(excel_row, 0, id)
            w.write(excel_row, 0, buyer)
            w.write(excel_row, 0, time)
            w.write(excel_row, 0, price)
            w.write(excel_row, 0, orderId)
            w.write(excel_row, 0, payBack)
            w.write(excel_row, 0, status)

            excel_row += 1

        exist_file = os.path.exists('test.xls')

        if exist_file:
            os.remove(r'test.xls')

        ws.save('test.xls')

        # 返回文件给客户
        sio = StringIO()
        ws.save(sio)
        sio.seek(0)

        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test.xls'
        response.write(sio.getvalue())

        return response
