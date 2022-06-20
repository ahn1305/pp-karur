from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home" ),
    path('monthly-report/', views.monthlyreport, name='mr')

]
