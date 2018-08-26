from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
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
            visible.field.widget.attrs['class']='form-control'


class passwordValidationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("place_user")
        self.user = user
        super(passwordValidationForm, self).__init__(*args, **kwargs)

    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )

    error_messages = {
        'invalid_password': (
            "Please enter a correct password."
        ),
    }

    def clean_password(self):
        password = self.cleaned_data['password']
        if check_password(password, self.user.password):

            return password
        else:
            raise forms.ValidationError(
                self.error_messages['invalid_password']
            )


# class Convert_form(forms.Form):
#     CHOICES = [('select1', 'select 1'),
#                ('select2', 'select 2')]
#     avorite_fruit = forms.CharField(label='What is your favorite fruit?',
#                                     widget=forms.RadioSelect(choices=CHOICES, attrs={'class': 'btn btn-default btn-lg'}))
