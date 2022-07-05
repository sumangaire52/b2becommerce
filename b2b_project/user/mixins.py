from allauth.account.views import SignupView
from .forms import CustomSignupForm
from .models import Customer, Admin, Salesman

class CustomSignupView(SignupView):
  template_name = 'account/signup.html'
  success_url = ''  # profile specific success url
  form_class = CustomSignupForm
  profile_class = None  # profile class goes here

  def form_valid(self, form):
    response = super(CustomSignupView, self).form_valid(form)
    if self.profile_class == Customer:
        self.user.is_customer = True

    if self.profile_class == Admin:
        self.user.is_admin = True
        
    if self.profile_class == Salesman:
        self.user.is_salesman = True

    user_type = self.profile_class(user=self.user, 
                                   full_name = form.cleaned_data['full_name'],
                                   address = form.cleaned_data['address'],
                                   contact_no = form.cleaned_data['contact_no'])
    user_type.save()

    return response