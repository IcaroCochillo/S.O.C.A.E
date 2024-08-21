# Generated by Django 5.0.2 on 2024-08-20 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(help_text='Digite a descrição do material', verbose_name='Descrição')),
                ('arquivo', models.FileField(blank=True, help_text='Selecione um arquivo', null=True, upload_to='materiais/', verbose_name='Arquivo')),
                ('titulo', models.CharField(help_text='Digite o título do material', max_length=100, verbose_name='Título')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materia.materia')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
            },
        ),
    ]
