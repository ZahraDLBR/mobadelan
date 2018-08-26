import re

from django import forms
from django.db import transaction
from django.forms import ModelForm

from core.models import User, Contact_msg

#
# class Contact_form(Mpdelform):
#     email = forms.EmailField()
#     phone = forms.CharField( phone_number = forms.RegexField(regex=r'^\+?1?\d{9}$',
#                                 error_message = ("Phone number must be entered in the format: '09123456789'.")))
#     name = forms.CharField(max_length=60)
#     text = forms.CharField(widget=forms.Textarea)
#
#     def __init__(self, *args, **kwargs):
#         super(Contact_form, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class']='form-control'
# #
# class Contact_form(Mpdelform):
#     email = forms.EmailField()
#     phone = forms.CharField( phone_number = forms.RegexField(regex=r'^\+?1?\d{9}$',
#                                 error_message = ("Phone number must be entered in the format: '09123456789'.")))
#     name = forms.CharField(max_length=60)
#     text = forms.CharField(widget=forms.Textarea)
#
#     def __init__(self, *args, **kwargs):
#         super(Contact_form, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class']='form-control'
#




class ContactForm(ModelForm):
    error_messages = {
        'invalid_phone': (
            "Phone number must be entered in the format: '09123456789'."
        ),
    }
    class Meta:
        model = Contact_msg
        fields = ['name', 'email', 'phone', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': "Type your message here..."}),
            'email': forms.TextInput(attrs={'placeholder': "Email"}),
            'phone': forms.TextInput(attrs={'placeholder': "Phone"}),
            'name': forms.TextInput(attrs={'placeholder': "Name"}),

        }


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']='form-control'



    def save(self, commit=True):
        msg = super(ContactForm, self).save(commit=True)
        return msg

    def clean_phone(self):
        phone =  self.cleaned_data['phone']
        pattern =re.compile("^\+?1?\d{11}$")
        if pattern.match(phone):
            return phone
        raise forms.ValidationError(
            self.error_messages['invalid_phone']
        )
