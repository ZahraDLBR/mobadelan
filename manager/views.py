from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.models import User, Staff
# Create your views here.
from django.views.generic import CreateView

from core.models import Contact_msg
from manager.forms import StaffSignUpForm


def managerpanel(request):
    return render(request, 'manager/managerpanel.html', context=None)

def comments(request):
    latest_comments = Contact_msg.objects.all()
    context = {'latest_comments': latest_comments}
    return render(request, 'manager/comments.html', context)

#def signupworker(request):
#    return render(request, 'manager/signupworker.html', context=None)

class signupworker(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'manager/signupworker.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/manager/')

def accountcirculation(request):
    return render(request, 'manager/accountcirculation.html', context=None)

def managerwallet(request):
    return render(request, 'manager/managerwallet.html', context=None)

def monitorworker(request):
    staff_information = Staff.objects.all()
    context = {'staff_information': staff_information}
    return render(request, 'manager/monitorworker.html', context)
    #return render(request, 'manager/monitorworker.html', context=None)

def monitorworkertransaction(request):
    return render(request, 'manager/monitorworkertransaction.html', context=None)


def monitorworkerinformation(request):
    staff_information = Staff.objects.all()
    context = {'staff_information': staff_information}
    return render(request, 'manager/monitorworkerinformation.html', context)
    #return render(request, 'manager/monitorworkerinformation.html', context=None)

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


def seencomment(request, msg_id):
    comment = Contact_msg.objects.get(pk=msg_id)
    comment.seen = True
    comment.save()

    return redirect('/manager/')

def parsedropdown(request, staff_id):
    comment = Contact_msg.objects.get(pk=staff_id)
    comment.seen = True
    comment.save()

    return redirect('/manager/monitorworker')

