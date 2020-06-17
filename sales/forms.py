from django import forms
from .models import Customer
from .models import Sale
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class RegisterCustomerForm(forms.ModelForm):
    customer_name = forms.CharField(label='Nome', min_length=2, max_length=200)

    def __init__(self, *args, **kwargs):
        super(RegisterCustomerForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

    def clean_customer_name(self):
        if len(self.cleaned_data['customer_name']) < 3:
            raise forms.ValidationError(u'O nome deve conter mais de 3 caracteres')
        else:
            return self.cleaned_data['customer_name']

    class Meta:
        model = Customer
        fields = ('customer_name', 'customer_location', 'customer_reference', 'customer_phone', 'customer_email')


class RegisterSaleForm(forms.ModelForm):
    pub_date = forms.DateTimeField(label='Data da venda')


    class Meta:
        model = Sale
        fields = ('customer', 'value', 'pub_date')


    def __init__(self, *args, **kwargs):
        super(RegisterSaleForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

