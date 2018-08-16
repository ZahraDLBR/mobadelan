from django.shortcuts import render


# Create your views here.


def workerpanel(request):
    return render(request, 'staff/workerpanel.html', context = None)

def transactionfromworker(request):
    return render(request, 'staff/transactionfromworker.html', context=None)

def connectforworker(request):
    return render(request, 'staff/connectforworker.html', context=None)
#def
#def Mainpage(request):
#    return render(request, 'staff/Mainpage.html', context=None)

def detail(request):
    return None
