from django.urls import path

from . import views

urlpatterns = [
	path('mqtt/', views.index),
	path('mqtt/<str:iotmodule>/<str:sensor>/', views.IotData)
]