from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomerSignUpForm
from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

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

def index(request):

    return render(request, 'customer/index.html', context={'user': request.user})
