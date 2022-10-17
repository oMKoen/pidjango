from django.urls import path

from . import views

urlpatterns = [
	path('mqtt/shellies', views.modulesconfigall),
	path('mqtt/shellies/2_5', views.shelly2_5moduleconfig),
	path('mqtt/shellies/2_5/', views.shelly2_5moduleconfig),
	path('mqtt/shellies/subscribetopics', views.getAllSubscribeTopics),
]