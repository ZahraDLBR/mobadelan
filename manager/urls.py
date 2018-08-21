from django.urls import path

from . import views

urlpatterns = [
    path('', views.managerpanel, name='managerpanel'),
    path('comments/', views.comments, name='comments'),
    path('signupworker/', views.signupworker, name='signupworker'),
    path('accountcirculation/', views.accountcirculation, name='accountcirculation'),
    path('managerwallet/', views.managerwallet, name='managerwallet'),
    path('monitorworker/', views.monitorworker, name='monitorworker'),
    path('sendnotif/', views.sendnotif, name='sendnotif'),
    path('monitoringuser/', views.monitoringuser, name='monitoringuser'),
    path('connect/', views.connect, name='connect'),
    path('monitorworker/workersalary/', views.workersalary, name='workersalary'),

]