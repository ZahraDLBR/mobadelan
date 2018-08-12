from django.shortcuts import render


# Create your views here.


def workerpanel(request):
    context = {
        'name': "workerpanel",
    }
    return render(request, 'templates/staff/workerpanel.html', context)

def detail(request):
    return None
