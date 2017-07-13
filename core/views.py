from django.shortcuts import render
import requests
import smtplib
from django.core.mail import send_mail

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
			envia(Alerta.objects.latest('period').email,'Seja bem vindo!')

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
		'alertas_count' : Alerta.objects.all().count()
	}
	return render(request, 'index.html', context)

def envia (destinatario, assunto):
	# Credenciais
	remetente    = 'smartpetbowl@gmail.com'
	senha        = 'smartpetbowl456'
	 
	# Informações da mensagem
	texto        = 'Praesent in mauris eu tortor porttitor accumsan. Mauris suscipit, ligula sit amet pharetra semper, nibh ante cursus purus, vel sagittis velit mauris vel metus. Aenean fermentum risus id tortor. Integer imperdiet lectus quis justo. Integer tempor. Vivamus ac urna vel leo pretium'
	 
	# Preparando a mensagem
	msg = '\r\n'.join([
	  'From: %s' % remetente,
	  'To: %s' % destinatario,
	  'Subject: %s' % assunto,
	  '',
	  '%s' % texto
	  ])
	 
	# Enviando o email
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(remetente,senha)
	server.sendmail(remetente, destinatario, msg)
	server.quit()

	Alerta.objects.create (email = destinatario, title = assunto, content = texto)


def update (request):

	reservatorio = Reservatorio.objects.latest ('period')

	if (reservatorio.nivel > 0):
		
		if (reservatorio.nivel<=2):
			#envia(Alerta.objects.latest('period').email,'O reservatorio do seu pet esta acabando')
			Alerta.objects.create (email = Alerta.objects.latest('period').email, title = 'O reservatorio do seu pet esta acabando')
			pass

		else:
			pass
		reservatorio.nivel = reservatorio.nivel-1
		reservatorio.save()
		
	else:
		#envia(Alerta.objects.latest('period').email,'O reservatorio do seu pet acabou')
		Alerta.objects.create (email = Alerta.objects.latest('period').email, title = 'O reservatorio do seu pet acabou')
		pass

	return render('index.html')

