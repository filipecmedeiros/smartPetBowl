from django.contrib import admin

from .models import Reservatorio, Agenda
# Register your models here.


class ReservatorioAdmin (admin.ModelAdmin):

	list_display = ['nivel', 'period']
	search_field = ['nivel', 'period']
	list_filter = ['period']


class AgendaAdmin (admin.ModelAdmin):

	list_display = ['agenda', 'period']
	search_field = ['agenda', 'period']
	list_filter = ['period']

admin.site.register (Reservatorio, ReservatorioAdmin)
admin.site.register (Agenda, AgendaAdmin)