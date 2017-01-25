from django import forms
from models import Contact
from django.core.mail import EmailMessage

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name','email','message',)
