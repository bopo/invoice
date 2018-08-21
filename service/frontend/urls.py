# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = (
    path('print/', views.report),
    path('excel/<int:id>', views.excel),
)
