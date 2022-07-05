from .mixins import CustomSignupView
from .models import Customer, Salesman, Admin

class CustomerSignupView(CustomSignupView):
   success_url = 'account_login'
   profile_class = Customer


class SalesmanSignupView(CustomSignupView):
    success_url = 'account_login'
    profile_class = Salesman

class AdminSignupView(CustomSignupView):
    success_url = 'account_login'
    profile_class = Admin