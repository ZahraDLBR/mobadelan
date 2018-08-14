from django.urls import path

from . import views

#paths
urlpatterns = [
    path('', views.workerpanel, name='workerpanel'),
    path('transactionfromworker/', views.transactionfromworker, name='transactionfromworker'),
    path('connectforworker/', views.connectforworker, name='connectforworker'),
#    path('Mainpage/', views.Mainpage, name='Mainpage'),

]
