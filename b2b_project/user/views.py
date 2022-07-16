from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from shop.decorators import admin_required
from .mixins import CustomSignupView
from .models import Customer, Salesman, Admin
from .forms import AdminSignupForm, CustomerSignupForm, SalesmanSignupForm

class CustomerSignupView(CustomSignupView):
   success_url = 'account_login'
   profile_class = Customer
   form_class = CustomerSignupForm


class SalesmanSignupView(CustomSignupView):
    success_url = reverse_lazy('shop:salesman_list')
    profile_class = Salesman
    form_class = SalesmanSignupForm

class AdminSignupView(CustomSignupView):
    success_url = 'account_login'
    profile_class = Admin
    form_class = AdminSignupForm