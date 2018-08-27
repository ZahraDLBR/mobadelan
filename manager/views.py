from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.models import User, Staff, Customer, Transaction, Manager, Message

from django.views.generic import CreateView
from django.contrib.auth.hashers import check_password
from django.utils import timezone

from core.models import Contact_msg
from manager.forms import StaffSignUpForm, salary_form, increasecredit_form, contacttostaff_form, contacttouser_form, \
    limitaccess_form
import datetime


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
    manager = Manager.objects.get(pk=10)
    if request.method == 'POST':
        form = increasecredit_form(request.POST)
        if form.is_valid():
            if check_password(form.cleaned_data['password'], manager.user.password):
                manager.credit += form.cleaned_data['increase_credit']
                manager.save()
        return redirect('/manager/')
    else:
        form = increasecredit_form()
    return render(request, 'manager/managerwallet.html', context={'form':form, 'manager' : manager})

    #manager = Manager.objects.get(pk=10)
    #return render(request, 'manager/managerwallet.html', context={'manager':manager})
    #return render(request, 'manager/managerwallet.html', context=None)

def monitorworker(request):
    staff_information = Staff.objects.all()
    context = {'staff_information': staff_information}
    return render(request, 'manager/monitorworker.html', context)
    #return render(request, 'manager/monitorworker.html', context=None)

def monitorworkertransaction(request, staff_id):
    staff_information = Staff.objects.all()
    staff = Staff.objects.get(pk=staff_id)
    transaction_information = Transaction.objects.all()
    return render(request, 'manager/monitorworkertransaction.html', context={'selected_staff' : staff, 'staff_information' : staff_information, 'transaction_information' : transaction_information})
    #return render(request, 'manager/monitorworkertransaction.html', context=None)


def monitorworkerinformation(request, staff_id):
    staff_information = Staff.objects.all()
    staff = Staff.objects.get(pk=staff_id)
    return render(request, 'manager/monitorworkerinformation.html', context={'selected_staff' : staff, 'staff_information' : staff_information})
    #return render(request, 'manager/monitorworkerinformation.html', context=None)

def monitorworkerlimitaccess(request, staff_id):
    if request.method == 'POST':
        form = limitaccess_form(request.POST)
        if form.is_valid():
            staff = Staff.objects.get(pk=staff_id)
            staff.user.is_active = False
            staff.ban_expiration_date = timezone.now() + datetime.timedelta(minutes=form.cleaned_data['minute'])
            staff.save()

        return redirect('/manager/')
    else:
        form = limitaccess_form()
    return render(request, 'manager/monitorworkerlimitaccess.html', context={'form':form})
    #return render(request, 'manager/monitorworkerlimitaccess.html', context=None)

def monitorworkerban(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    staff.user.is_active = False
    staff.user.save()

    return redirect('/manager/monitorworker/')
    #return render(request, 'manager/monitorworker.html', context=None)

def sendnotif(request):
    return render(request, 'manager/sendnotif.html', context=None)

def monitoringuser(request):
    user_information = Customer.objects.all()
    context = {'user_information': user_information}
    return render(request, 'manager/monitoringuser.html', context)
    #return render(request, 'manager/monitoringuser.html', context=None)

def monitoringusertransaction(request, customer_id):
    user_information = Customer.objects.all()
    selected_user = Customer.objects.get(pk=customer_id)
    transaction_information = Transaction.objects.all()
    return render(request, 'manager/monitoringusertransaction.html', context={'selected_user' : selected_user, 'user_information' : user_information, 'transaction_information' : transaction_information})
    #return render(request, 'manager/monitoringusertransaction.html', context=None)

def monitoringuserinformation(request, customer_id):
    selected_user = Customer.objects.get(pk=customer_id)
    user_information = Customer.objects.all()

    return render(request, 'manager/monitoringuserinformation.html', context={'selected_user' : selected_user, 'user_information' : user_information})

    #return render(request, 'manager/monitoringuserinformation.html', context=None)

def monitoringuserlimitaccess(request):
    return render(request, 'manager/monitoringuserlimitaccess.html', context=None)

def monitoringuserban(request, customer_id):
    selected_user = Customer.objects.get(pk=customer_id)
    selected_user.user.is_active = False
    selected_user.user.save()

    return redirect('/manager/monitoringuser/')


#def contacttostaff1(request):
#    staff_information = Staff.objects.all()
#    context = {'staff_information': staff_information}
#    return render(request, 'manager/contacttostaff.html', context)



def contacttostaff(request):

    if request.method == 'POST' :
        form = contacttostaff_form(request.POST)
        if form.is_valid():


            if form.cleaned_data['send_to_all']:
                for staff in Staff.objects.all():
                    msg = Message(sender=Manager.objects.get(pk=10).user, receiver=staff.user, create_time=datetime.datetime.now(), text=form.cleaned_data['text'], seen=False)
                    msg.save()

            else:
                if form.cleaned_data['receiver'] != None:
                    staff = Staff.objects.get(pk=form.cleaned_data['receiver'])
                    msg = Message(sender = Manager.objects.get(pk=10).user, receiver = staff.user, create_time = datetime.datetime.now(), text = form.cleaned_data['text'], seen = False)
                    msg.save()

        if form.cleaned_data['receiver'] != None or form.cleaned_data['send_to_all']:
            return redirect('/manager/')
    else:
        form = contacttostaff_form()

    staff_information = Staff.objects.all()
    context = {'staff_information': staff_information, 'form' : form}
    return render(request, 'manager/contacttostaff.html', context)
    #return render(request, 'manager/contacttostaff.html', context=None)

def contacttouser(request):

    if request.method == 'POST' :
        form = contacttouser_form(request.POST)
        if form.is_valid():

            if form.cleaned_data['send_to_all']:
                for customer in Customer.objects.all():
                    msg = Message(sender=Manager.objects.get(pk=10).user, receiver=customer.user, create_time=datetime.datetime.now(), text=form.cleaned_data['text'], seen=False)
                    msg.save()
            else:
                if form.cleaned_data['receiver'] != None:
                    customer = Customer.objects.get(pk=form.cleaned_data['receiver'])
                    msg = Message(sender = Manager.objects.get(pk=10).user, receiver = customer.user, create_time = datetime.datetime.now(), text = form.cleaned_data['text'], seen = False)
                    msg.save()
        if form.cleaned_data['receiver'] != None or form.cleaned_data['send_to_all']:
            return redirect('/manager/')
    else:
        form = contacttouser_form()

    user_information = Customer.objects.all()
    context = {'user_information': user_information, 'form' : form}
    return render(request, 'manager/contacttouser.html', context)




def workersalary(request, staff_id):
    if request.method == 'POST':
        form = salary_form(request.POST)
        if form.is_valid():
            staff = Staff.objects.get(pk=staff_id)
            staff.salary = form.cleaned_data['salary']
            staff.save()
        return redirect('/manager/')
    else:
        form = salary_form()
    return render(request, 'manager/workersalary.html', context={'form':form})
    #return render(request, 'manager/workersalary.html', context=None)


def seencomment(request, msg_id):
    comment = Contact_msg.objects.get(pk=msg_id)
    comment.seen = True
    comment.save()

    return redirect('/manager/')

def parsedropdowntostaff(request, staff_id):

    staff = Staff.objects.get(pk=staff_id)
    staff_information = Staff.objects.all()

    return render(request, 'manager/monitorworker.html', context={'selected_staff' : staff, 'staff_information' : staff_information})

def parsedropdowntouser(request, customer_id):
    selected_user = Customer.objects.get(pk=customer_id)
    user_information = Customer.objects.all()

    return render(request, 'manager/monitoringuser.html', context={'selected_user' : selected_user, 'user_information' : user_information})




    #is_staff = False
    #is_customer = False
    #reciever = User.objects.get(pk=reciever_id)
    #if reciever.is_staff:
    #    is_staff = True
    #    reciever = Staff.objects.get(pk=reciever_id)
    #    reciever_information = Staff.objects.all()
    #    return render(request, 'manager/contacttostaff.html', context={'staff': reciever, 'staff_information': reciever_information, 'is_staff': is_staff, 'is_customer': is_customer, 'selected' : True})

    #else:
    #    is_customer = True
    #    reciever = Customer.objects.get(pk=reciever_id)
    #    reciever_information = Customer.objects.all()

    #    return render(request, 'manager/connect.html', context={'user' : reciever, 'user_information' : reciever_information, 'is_staff' : is_staff, 'is_customer' : is_customer, 'selected' : True})






