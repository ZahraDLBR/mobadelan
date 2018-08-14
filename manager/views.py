from django.shortcuts import render

# Create your views here.


def managerpanel(request):
    return render(request, 'manager/managerpanel.html', context=None)

