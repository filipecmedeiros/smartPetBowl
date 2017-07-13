from django.shortcuts import render
import requests
import datetime

from .models import Reservatorio, Agenda, Alerta

from .forms import ReservatorioForm, AgendaForm, AlertaForm
# Create your views here.
def index (request):

	if request.method == 'POST':
		form_reservatorio = ReservatorioForm(request.POST)
		form_agenda = AgendaForm(request.POST)
		form_alerta = AlertaForm (request.POST)

		if form_reservatorio.is_valid():
			nivel = form_reservatorio.cleaned_data['nivel']
			Reservatorio.objects.create(nivel = nivel)


		if form_agenda.is_valid():
			agenda = form_agenda.cleaned_data['agenda']
			Agenda.objects.create(agenda = agenda)

		if form_alerta.is_valid():
			email = form_alerta.cleaned_data ['email']
			Alerta.objects.create(email = email)

	else:
		form_reservatorio = ReservatorioForm()
		form_agenda = AgendaForm()
		form_alerta = AlertaForm()


	reservatorio = Reservatorio.objects.latest ('period')
	agenda = Agenda.objects.latest ('period')
	alertas = Alerta.objects.all().order_by('-id')[:5]
	context = {
		'reservatorio' : reservatorio,
		'agenda' : agenda,
		'form_reservatorio' : form_reservatorio,
		'form_agenda' : form_agenda,
		'form_alerta' : form_alerta,
		'alertas' : alertas,
	}
	return render(request, 'index.html', context)

def update (request):

	reservatorio = Reservatorio.objects.latest ('period')

	if (reservatorio.nivel > 0):
		
		if (reservatorio.nivel<=2):
			print ('email')

		reservatorio.nivel = reservatorio.nivel-1
		reservatorio.save()

	return render('index.html')