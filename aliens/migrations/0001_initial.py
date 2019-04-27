# Generated by Django 2.2 on 2019-04-27 19:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=2, verbose_name='Sigla')),
                ('name', models.CharField(max_length=50, verbose_name='Estado')),
                ('count', models.IntegerField(default=0, verbose_name='Total de Eventos')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['initials'],
            },
        ),
        migrations.CreateModel(
            name='Alien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Data')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='state_fk', to='aliens.State', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Ocorrência',
                'verbose_name_plural': 'Ocorrências',
            },
        ),
    ]
