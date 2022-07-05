from django import forms
from user.models import Admin
from shop.models import Product

class AdminProfileEditform(forms.ModelForm): 
    class Meta:
        model = Admin
        fields = ['full_name', 'contact_no', 'address']

class AddProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
        self.fields['sub_category'].widget.attrs.update({'class': 'form-select'})
        self.fields['sub_sub_category'].widget.attrs.update({'class': 'form-select'})
        self.fields['brand'].widget.attrs.update({'class': 'form-select'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['color'].widget.attrs.update({'class': 'form-select'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['discounted_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['stock'].widget.attrs.update({'class': 'form-control'})
        self.fields['size'].widget.attrs.update({'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Product
        fields = '__all__'
    