from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.is_customer:
            return redirect('customer:index')
        elif request.user.is_staff:
            return redirect('staff:index')
        elif request.user.is_manager:
            return redirect('manager:managerpanel')
    return render(request, 'core/home.html')