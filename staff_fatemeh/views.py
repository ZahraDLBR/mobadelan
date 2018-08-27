from django.shortcuts import render


# Create your views here.
from core.models import Staff


def workerpanel(request):
    return render(request, 'staff/workerpanel.html', context = None)

def transactionfromworker(request):
    return render(request, 'staff/transactionfromworker.html', context=None)

def connectforworker(request):
    return render(request, 'staff/connectforworker.html', context=None)
#def
#def Mainpage(request):
#    return render(request, 'staff/home.html', context=None)

def detail(request):
    return None

def about(request):
    return None


def Informationworker(request):
    worker_infomation = Staff.objects.all()
    context = { 'worker_infomation':worker_infomation}
    return render(request,'staff/Informationworker',context)

def dolar(request):
	#response = request.get('http://www.faranevis.com/api/currency')
	#MyData = response.json()
	#Dollar = MyData['دلار']
	#Euro = MyData['یورو']
	#context = { 'Dollar':Dollar, 'Euro':Euro}
	#return render(request, 'staff/dolar.html', context)
    return None

def cntrltransaction(request):
    return None

def Contact(request):
    request.post.get()
