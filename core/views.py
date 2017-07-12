from django.shortcuts import render
import requests
import datetime

from .models import Reservatorio, Agenda

from .forms import ReservatorioForm, AgendaForm
# Create your views here.
def index (request):

	if request.method == 'POST':
		form_reservatorio = ReservatorioForm(request.POST)
		form_agenda = AgendaForm(request.POST)

		if form_reservatorio.is_valid():
			nivel = form_reservatorio.cleaned_data['nivel']
			Reservatorio.objects.create(nivel = nivel)


		if form_agenda.is_valid():
			agenda = form_agenda.cleaned_data['agenda']
			Agenda.objects.create(agenda = agenda)
	else:
		form_reservatorio = ReservatorioForm()
		form_agenda = AgendaForm()


	reservatorio = Reservatorio.objects.latest ('period')
	agenda = Agenda.objects.latest ('period')
	context = {
		'reservatorio' : reservatorio,
		'agenda' : agenda,
		'form_reservatorio' : form_reservatorio,
		'form_agenda' : form_agenda
	}
	return render(request, 'index.html', context)