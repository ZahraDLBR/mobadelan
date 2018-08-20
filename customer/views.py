from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomerSignUpForm
from django.views.generic import CreateView

from core.models import User


class StudentSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('customer.panel')


def index(request):
    context = {
        'name': "zahra",
    }
    return render(request, 'customer/index.html', context)
