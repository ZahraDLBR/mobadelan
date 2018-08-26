from django.urls import path, include

import customer
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/tanks/', views.tanks, name='tanks'),
    path('about/', views.about, name='about'),

    # path('accounts/', include('django.contrib.auth.urls')),

]