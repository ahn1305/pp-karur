from django.urls import path
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path('dailyreport/', views.dailyreport, name='dr'),
    path('monthlyreport/', views.monthlyreport, name='mr'),
    path('semreport/', views.semreport, name='sr')

]
