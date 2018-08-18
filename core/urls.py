from django.urls import path

import customer
from . import views

urlpatterns = [
    path('', views.Mainpage, name='Mainpage'),

]