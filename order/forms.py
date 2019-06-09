from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Dhaka', 'Dhaka'),
		('Chattagram', 'Chattagram'),
		('Rajshahi', 'Rajshahi '),
	)

	DISCRICT_CHOICES = (
		('Dhaka', 'Dhaka'), 
		('Gazipur', 'Gazipur'),
		('Narayanganj', 'Narayanganj'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Rocket', 'Rocket'),
		('Bkash','Bkash')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
