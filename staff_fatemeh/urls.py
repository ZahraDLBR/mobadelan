from django.urls import path, include

from . import views



#paths

urlpatterns = [

    path('', include(([
                          path('', views.workerpanel, name='workerpanel'),
                          path('transactionfromworker/', views.transactionfromworker, name='transactionfromworker'),
                          path('connectforworker/', views.connectforworker, name='connectforworker'),
                          path('cntrltransaction/', views.cntrltransaction, name='ccntrltransaction'),
                          path('Informationworker/', views.Informationworker, name='Informationworker'),
                          path('dolar/', views.dolar, name='dolar'),
                           ], 'staff'), namespace='staff')),



]
