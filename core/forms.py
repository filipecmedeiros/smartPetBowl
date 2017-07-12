from django import forms


class ReservatorioForm (forms.Form):

	nivel = forms.IntegerField(label='Capacidade')

class AgendaForm (forms.Form):
	
	agenda = forms.IntegerField(label='Agendar para a cada')
