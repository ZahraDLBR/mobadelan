from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Mainpage(request):
    return render(request, 'core/Mainpage.html', context=None)