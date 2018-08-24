from django.urls import path, include

import customer
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('accounts/', include('django.contrib.auth.urls')),

]