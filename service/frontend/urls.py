# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = (
    path('report/', views.report),
    path('excels/<int:id>', views.excels),
)
