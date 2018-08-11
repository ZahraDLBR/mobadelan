from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': "zahra",
    }
    return render(request, 'customer/index.html', context)
