# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cidade_UF', models.CharField(max_length=2, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('cidade_Nome', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('pess_Nome', models.CharField(max_length=50, blank=True)),
                ('pess_DtNascimento', models.DateField()),
                ('pess_NomePai', models.CharField(max_length=50, blank=True)),
                ('pess_NomeMae', models.CharField(max_length=50, blank=True)),
                ('pess_Endereco', models.CharField(max_length=50, blank=True)),
                ('pess_Numero', models.CharField(max_length=10, blank=True)),
                ('pess_Complemento', models.CharField(max_length=50, blank=True)),
                ('pess_Bairro', models.CharField(max_length=50, blank=True)),
                ('pess_CEP', models.CharField(max_length=8, blank=True)),
                ('pess_CPF', models.CharField(max_length=11, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('pessoa_ptr', models.OneToOneField(serialize=False, to='core.Pessoa', auto_created=True, parent_link=True, primary_key=True)),
                ('nomePai', models.CharField(max_length=50)),
                ('nomeMae', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=('core.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='pess_Cidade',
            field=models.ForeignKey(to='core.Cidade', blank=True),
            preserve_default=True,
        ),
    ]
