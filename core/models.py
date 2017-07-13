from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.


class Reservatorio (models.Model):

	nivel = models.IntegerField ('Nivel')
	period = models.DateTimeField('Coletado em', auto_now_add=True)

	class Meta:
		verbose_name = 'Reservatório'
		verbose_name_plural = 'Coletas do reservatório'
		ordering = ['period']


class Agenda (models.Model):

	agenda = models.IntegerField ('A cada ')
	period = models.DateTimeField('Agendado em', auto_now_add=True)

	class Meta:
		verbose_name = 'Agendamento da dieta'
		verbose_name_plural = 'Histórico de agendamento'
		ordering = ['period']

class Alerta (models.Model):

	email = models.EmailField ('Email')
	created = models.DateTimeField('Cadastrado em', auto_now_add=True)
	
	title = models.CharField ('Titulo', max_length=100, blank=True)
	content = models.CharField ('Conteudo', max_length=500, blank=True)
	period = models.DateTimeField ('Enviado em', auto_now=True)


	class Meta:
		verbose_name = 'Cadastro de alertas'
		verbose_name_plural = 'Histórico de cadastro de alertas'
		ordering = ['period']