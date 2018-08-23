from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from core.models import User, Customer


class StaffSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'user', 'email', 'phone_number')
        # widgets = {
        #     'myfield': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user

    def __init__(self, *args, **kwargs):
        super(CustomerSignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'