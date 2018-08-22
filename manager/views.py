from django.shortcuts import render

# Create your views here.


def managerpanel(request):
    return render(request, 'manager/managerpanel.html', context=None)

def comments(request):
    return render(request, 'manager/comments.html', context=None)

def signupworker(request):
    return render(request, 'manager/signupworker.html', context=None)


def accountcirculation(request):
    return render(request, 'manager/accountcirculation.html', context=None)

def managerwallet(request):
    return render(request, 'manager/managerwallet.html', context=None)

def monitorworker(request):
    return render(request, 'manager/monitorworker.html', context=None)

def monitorworkertransaction(request):
    return render(request, 'manager/monitorworkertransaction.html', context=None)


def monitorworkerinformation(request):
    return render(request, 'manager/monitorworkerinformation.html', context=None)

def monitorworkerlimitaccess(request):
    return render(request, 'manager/monitorworkerlimitaccess.html', context=None)

def sendnotif(request):
    return render(request, 'manager/sendnotif.html', context=None)

def monitoringuser(request):
    return render(request, 'manager/monitoringuser.html', context=None)

def monitoringusertransaction(request):
    return render(request, 'manager/monitoringusertransaction.html', context=None)

def monitoringuserinformation(request):
    return render(request, 'manager/monitoringuserinformation.html', context=None)

def monitoringuserlimitaccess(request):
    return render(request, 'manager/monitoringuserlimitaccess.html', context=None)

def connect(request):
    return render(request, 'manager/connect.html', context=None)

def workersalary(request):
    return render(request, 'manager/workersalary.html', context=None)