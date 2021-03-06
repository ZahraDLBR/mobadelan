from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm, Textarea, ModelChoiceField

from core.models import User, Staff, Message


class StaffSignUpForm(UserCreationForm):

    salary = forms.IntegerField()
    phone_number = forms.RegexField(regex=r'^\+?1?\d{11}$',
                                    help_text=(
                                    "Phone number must be entered in the format: '09123456789'"))
    bank_account_number = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'bank_account_number', 'phone_number', 'salary')
        # widgets = {
        #     'myfield': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        staff = Staff.objects.create(user=user)
        return user


class salary_form(forms.Form):
    salary = forms.IntegerField()

class limitaccess_form(forms.Form):
    minute = forms.IntegerField()


class increasecredit_form(forms.Form):
    increase_credit = forms.IntegerField()
    password = forms.CharField(label="password", strip=False, widget=forms.PasswordInput)



class contacttostaff_form(forms.Form):
    text = forms.CharField(widget=Textarea(attrs={'cols': 110, 'rows': 10, 'class': "textarea_editor span12"}))
    receiver = forms.ModelChoiceField(queryset=User.objects.filter(is_staff = True),widget=forms.Select(attrs={'class' : "btn btn-success dropdown-toggle"}), required=False)
    send_to_all = forms.BooleanField(initial=False, required=False)

class contacttouser_form(forms.Form):
    text = forms.CharField(widget=Textarea(attrs={'cols': 110, 'rows': 10, 'class': "textarea_editor span12"}))
    receiver = forms.ModelChoiceField(queryset=User.objects.filter(is_customer = True),widget=forms.Select(attrs={'class' : "btn btn-success dropdown-toggle"}), required=False)
    send_to_all = forms.BooleanField(initial=False, required=False)

