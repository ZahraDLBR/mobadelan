from django.urls import path

from . import views

urlpatterns = [
    path('workerpanel/', views.workerpanel, name='workerpanel'),

]