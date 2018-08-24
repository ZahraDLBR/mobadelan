from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.exceptions import NON_FIELD_ERRORS

from core.models import User, Customer


class CustomerSignUpForm(UserCreationForm):

    bank_account_number = forms.CharField(max_length=16)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                    help_text= "Phone number must be entered in the format: '09123456789'.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'bank_account_number', 'phone_number')
        # widgets = {
        #     'myfield': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        # user.is_active = False
        user.save()
        customer = Customer.objects.create(user=user)
        customer.bank_account_number = self.cleaned_data.get('bank_account_number')
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.save()
        return user

    def __init__(self, *args, **kwargs):
        super(CustomerSignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'