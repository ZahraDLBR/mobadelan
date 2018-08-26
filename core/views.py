from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.generic import FormView

from core.forms import ContactForm


def home(request):
    if request.user.is_authenticated:
        if request.user.is_customer:
            return redirect('customer:index')
        elif request.user.is_staff:
            return redirect('staff:index')
        elif request.user.is_manager:
            return redirect('manager:managerpanel')
    return render(request, 'core/home.html')


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = 'tanks/'


    def get_context_data(self, **kwargs):
        kwargs['name'] = "zahra"
        return super().get_context_data(**kwargs)


def tanks(request):

    return HttpResponse("tanks")