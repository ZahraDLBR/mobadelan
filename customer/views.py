from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
# from django.core.serializers import json
from django.db import transaction
from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CustomerSignUpForm, passwordValidationForm
from django.views.generic import CreateView, FormView
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from core.models import User, Manager, Transaction, Customer

import urllib.request, json

class StudentSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # current_site = "mobadelan"
        # mail_subject = 'Activate your blog account.'
        # message = render_to_string('customer/acc_active_email.html', {
        #     'user': user,
        #     'domain': "mobadelan",
        #     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        #     'token': account_activation_token.make_token(user),
        # })
        # to_email = form.cleaned_data.get('email')
        # email = EmailMessage(
        #     mail_subject, message, to=[to_email]
        # )
        # email.send()
        # return HttpResponse('Please confirm your email address to complete the registration')
        login(self.request, user)
        return redirect('customer:index')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

# class indecxView(FormView):
#     form_class = Convert_form
#     template_name = 'customer/index.html'
#
#     def get_success_url(self):
#         return HttpResponse("hi")
def index(request):

    if request.method == 'POST':

        if request.session['getJdata'] == False:
            with urllib.request.urlopen("http://www.faranevis.com/api/currency") as url:
                data = json.loads(url.read().decode())
            request.session['Jdata'] = data
            request.session['getJdata'] = True

        # response = r('http://www.faranevis.com/api/currency')
        data = request.session['Jdata']
        value = {'$usa': data['دلار']['قیمت'], '$canada':data['دلار کانادا']['قیمت'], '$australia':data['دلار استرالیا']['قیمت'],'pound':data['پوند']['قیمت'],
                 'euro':data['یورو']['قیمت'], 'Swissfranc':data['فرانک سوئیس']['قیمت'],}


        number = request.POST.get('unit')
        print(number)
        if not number:
            number = 0
        unit = value.get(request.POST.get('selector')).replace(',', '')

        return render(request, 'customer/index.html', context={'amount': int(unit) * int(number),'number': number, 'unit':request.POST.get('selector')})
    request.session['getJdata'] = False
    return render(request, 'customer/index.html', context={'user': request.user})


class commissionView(FormView):

    template_name = 'customer/commission.html'

    form_class = passwordValidationForm
    # success_url = 'tanks/'


    #
    # def get_form_kwargs(self):
    #     kwargs = super(commissionView, self).get_form_kwargs()
    #     kwargs.update({'request': self.request})
    #
    #    return kwargs

    def get_success_url(self):
        return reverse('customer:tanks')


    def get_form_kwargs(self):
        kwargs = super(commissionView, self).get_form_kwargs()
        kwargs.update({"place_user": self.request.user,})
        return kwargs

    def form_valid(self, form):
        print("in valid")
        amount = self.kwargs['amount']
        type = self.kwargs['type']
        do_transactions(self.request, amount, type)
        return super().form_valid(form)



@transaction.atomic
def do_transactions(request, amount, type):
    manager = Manager.objects.get(pk=10)
    customer = Customer.objects.get(pk=request.user)
    customer.credit -= amount
    manager.credit += amount
    customer.save()
    manager.save()
    transaction = Transaction()
    transaction. value = amount
    transaction.creator = customer
    transaction.state ='W'
    transaction.transactions_type=type
    transaction.save()
    request.session['trans_id']= transaction.id


def tank(request):

    return HttpResponse(request.session['trans_id'])

#
# def doTransactions(request):
#     return None