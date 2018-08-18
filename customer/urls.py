from django.urls import path, include

from . import views


urlpatterns = [
    path('', include(([
        path('', views.index, name='index'),
        path('signup/', views.StudentSignUpView.as_view(), name='signup'),
    ],'customer'), namespace='customer')),

]
