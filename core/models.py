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
	period = models.DateTimeField('Coletado em', auto_now_add=True)

	class Meta:
		verbose_name = 'Agendamento da dieta'
		verbose_name_plural = 'Histórico de agendamento'
		ordering = ['period']