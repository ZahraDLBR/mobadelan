from django.urls import path, include

from . import views



#paths

urlpatterns = [

    path('', include(([
                          path('', views.workerpanel, name='workerpanel'),
                          path('transactionfromworker/', views.transactionfromworker, name='transactionfromworker'),
                          path('connectforworker/', views.connectforworker, name='connectforworker'),

                           ], 'staff'), namespace='staff')),



]
