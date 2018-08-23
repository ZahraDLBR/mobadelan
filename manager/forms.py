from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from core.models import User, Staff

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
