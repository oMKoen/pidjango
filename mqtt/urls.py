from django.urls import include, path

from . import views

urlpatterns = [
	path('mqtt/', views.index),
#	path('mqtt/<str:iotmodule>/<str:sensor>/', views.IotData),
	path('modulesconfig', views.modulesconfigall),
	path('modulesconfig/<str:modulesconfig', views.modulesconfig),
	path('modulesconfig/<str:modulesconfig>/<str:version>', views.modulesconfig),
    path('', include('mqtt.Shellies.urls')),
]