from django.conf.urls import url
from django.urls import path, include

from . import views


urlpatterns = [
    path('', include(([
        path('', views.index, name='index'),
        path('signup/', views.StudentSignUpView.as_view(), name='signup'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    ],'customer'), namespace='customer')),

]
