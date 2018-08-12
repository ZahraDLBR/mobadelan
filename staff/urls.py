from django.urls import path

from . import views

#paths
urlpatterns = [
    path('workerpanel', views.workerpanel, name='workerpanel'),

]