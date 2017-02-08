from django.shortcuts import render
from forms import ContactForm
from models import Content, Contact

def index(request):
	queryset = Content.objects.all()
	context = {
		"obj_list": queryset,
	}
	return render(request, 'index.html', context)

def site(request, slug):
	image = Content.objects.get(slugger=slug)
	print image
	context={
		"obj": image,
	}
	return render(request, 'site.html', context)

def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		print 'Idle...'
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			form.send_message()
			print 'Upload Complete'
		else:
			print 'Error: MESSAGE FAILED TO SEND!'
	return render(request, 'contact.html', {'form' : form})

def about(request):
	return render(request, 'about.html')

