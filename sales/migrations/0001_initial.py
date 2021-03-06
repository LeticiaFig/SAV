# Generated by Django 3.0.4 on 2020-04-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200, verbose_name='Nome')),
                ('customer_location', models.CharField(blank=True, max_length=200, verbose_name='Endereço')),
                ('customer_reference', models.CharField(blank=True, max_length=200, verbose_name='Referência')),
                ('customer_email', models.EmailField(blank=True, max_length=200, verbose_name='Email')),
                ('customer_phone', models.CharField(blank=True, max_length=200, verbose_name='Telefone')),
                ('pub_date', models.DateTimeField(verbose_name='Data de Cadastro')),
            ],
        ),
    ]
