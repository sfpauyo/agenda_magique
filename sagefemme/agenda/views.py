from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Appointment


def index(request):
	#TODO : limit the number of appointment
	appointment_list = Appointment.objects.all()
	context={
		'appointment_list': appointment_list
	}
	template = loader.get_template('agenda/calendar_design.html')
	return HttpResponse(template.render(context,request))
