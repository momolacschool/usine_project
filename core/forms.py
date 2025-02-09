from django import forms
from .models import Order, Contact

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "customer_name", "customer_email", "quantity"]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message"]
