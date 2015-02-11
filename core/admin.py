from django.contrib import admin
from core.models import Candidato, Cidade

# Register your models here.

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pess_Nome', 'pess_CPF','pess_NomePai', 'pess_NomeMae')

admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Cidade)