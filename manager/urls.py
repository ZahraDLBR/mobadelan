from django.urls import path

from . import views

urlpatterns = [
    path('', views.managerpanel, name='managerpanel'),
    path('comments/', views.comments, name='comments'),
    path('signupworker/', views.signupworker.as_view(), name='signupworker'),
    path('accountcirculation/', views.accountcirculation, name='accountcirculation'),
    path('managerwallet/', views.managerwallet, name='managerwallet'),
    path('monitorworker/', views.monitorworker, name='monitorworker'),
    path('sendnotif/', views.sendnotif, name='sendnotif'),
    path('monitoringuser/', views.monitoringuser, name='monitoringuser'),
    path('connect/', views.connect, name='connect'),
    path('monitorworker/workersalary/', views.workersalary, name='workersalary'),
    path('monitorworker/monitorworkertransaction/', views.monitorworkertransaction, name='monitorworkertransaction'),
    path('monitorworker/monitorworkerinformation/<int:staff_id>', views.monitorworkerinformation, name='monitorworkerinformation'),
    path('monitoringuser/monitoringusertransaction', views.monitoringusertransaction, name='monitoringusertransaction'),
    path('monitoringuser/monitoringuserinformation/<int:customer_id>', views.monitoringuserinformation, name='monitoringuserinformation'),
    path('monitoringuser/monitorworkerlimitaccess', views.monitorworkerlimitaccess, name='monitorworkerlimitaccess'),
    path('monitoringuser/monitoringuserlimitaccess', views.monitoringuserlimitaccess, name='monitoringuserlimitaccess'),
    path('seencomment/<int:msg_id>', views.seencomment, name='seencomment'),
    path('parsedropdowntostaff/<int:staff_id>', views.parsedropdowntostaff, name='parsedropdowntostaff'),
    path('parsedropdowntouser/<int:customer_id>', views.parsedropdowntouser, name='parsedropdowntouser'),


]