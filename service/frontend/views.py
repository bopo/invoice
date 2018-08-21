from django.shortcuts import render


def excels(request, id=None):
    return render(request, 'excel.html', locals())


def report(request):
    ids = request.GET('ids', [])

    return render(request, 'report.html', locals())
