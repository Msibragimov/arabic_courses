from django import forms
from django.core.validators import RegexValidator

from apps.customer.models import Customer


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon raqamizni quyidagi ko'rinishda kiriting: '+9989999999'. 15 raqamdan oshmasligi kerak.")
    phone_number = forms.IntegerField(validators=[phone_regex], required=True)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number']

    def __init__(self, *args, **kwargs) -> None:
        super(CustomerForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'First name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Last name'})
        self.fields['phone_number'].widget.attrs.update({'class':'form-control','placeholder':'Phone Number'})

    def save(self, commit=True):
        customer = super(CustomerForm, self).save(commit=False)
        if commit:
            customer.save()
        return customer
