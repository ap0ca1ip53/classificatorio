from django.db import models
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

class Cidade(models.Model):
	cidade_UF = models.CharField(max_length=2, choices=STATE_CHOICES)
	cidade_Nome = models.CharField(max_length=40)

	def __str__(self):
		return self.cidade_Nome


class Pessoa(models.Model):
	CHOICE_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))

	pess_Nome = models.CharField(max_length=50, blank=True)
	pess_DtNascimento = models.DateField()
	pess_NomePai = models.CharField(max_length=50, blank=True)
	pess_NomeMae = models.CharField(max_length=50, blank=True)
	pess_Endereco = models.CharField(max_length=50, blank=True)
	pess_Numero = models.CharField(max_length=10, blank=True)
	pess_Complemento = models.CharField(max_length=50, blank=True)
	pess_Bairro = models.CharField(max_length=50, blank=True)
	pess_CEP = models.CharField(max_length=8, blank=True)
	pess_Cidade = models.ForeignKey(Cidade, blank=True)
	pess_SEXO = models.CharField(max_length=2, choices=CHOICE_SEXO)
	pess_Email = models.EmailField()
	pess_FoneResidencial = models.CharField(max_length=)

	pess_CPF = models.CharField(max_length=11, blank=True)


	def __str__(self):
		return self.pess_Nome


class Candidato(Pessoa):
	nomePai = models.CharField(max_length=50)
	nomeMae = models.CharField(max_length=50)