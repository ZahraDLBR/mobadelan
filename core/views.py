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

    def form_valid(self, form):
        self.msg = form.save()
        return render(self.request, 'core/contact.html',
                      context={'msg': ("dear " + self.msg.name + " thanks for your message. it will be sent to magner"),'form': form})



def tanks(request):

    return HttpResponse("tanks")

def about(request):
    return render(request,'core/about.html')

def arz(request):
    return render(request,'core/arz.html')    

