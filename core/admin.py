from django.contrib import admin
from core.models import Candidato, Cidade

# Register your models here.

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pess_Nome', 'pess_CPF','cand_NomePai', 'cand_NomeMae')

class CidadeAdmin(admin.ModelAdmin):
	ordering = ['cidade_UF', 'cidade_Nome']
	list_display = ('id', 'cidade_UF', 'cidade_Nome')
	list_filter = ('cidade_UF',)

admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Cidade, CidadeAdmin)