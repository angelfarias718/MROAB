from django import forms
from models import Contact
from django.core.mail import EmailMessage

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name','email','message',)
	def send_message(self):
		email_msg = EmailMessage ('Message from 360 City','Theres a new message in your admin panel. Visit Localhost:8000/admin to see more', to=['sergioa.garcia217@gmail.com'])
		email_msg.send()
