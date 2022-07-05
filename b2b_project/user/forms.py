from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField
from django import forms
from .models import Customer

class CustomSignupForm(SignupForm):
    full_name = forms.CharField(max_length=100, label = 'Full Name')
    contact_no = PhoneNumberField(label = "Contact No.")
    address = forms.CharField(max_length=200, label = 'Address')

    def save(self, request,):
        user = super(CustomSignupForm, self).save(request)
        user.is_customer = True
        user.save()
        return user