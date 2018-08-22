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
    path('monitorworker/monitorworkertransaction/', views.monitorworkertransaction, name='monitorworkertransaction'),
    path('monitorworker/monitorworkerinformation/', views.monitorworkerinformation, name='monitorworkerinformation'),
    path('monitoringuser/monitoringusertransaction', views.monitoringusertransaction, name='monitoringusertransaction'),
    path('monitoringuser/monitoringuserinformation', views.monitoringuserinformation, name='monitoringuserinformation'),
    path('monitoringuser/monitorworkerlimitaccess', views.monitorworkerlimitaccess, name='monitorworkerlimitaccess'),
    path('monitoringuser/monitoringuserlimitaccess', views.monitoringuserlimitaccess, name='monitoringuserlimitaccess'),

]