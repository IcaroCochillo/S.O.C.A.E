# Generated by Django 5.0.2 on 2024-08-20 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(help_text='Digite o ano da turma', verbose_name='Ano')),
                ('nome_turma', models.CharField(help_text='Digite o nome da turma', max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
    ]
