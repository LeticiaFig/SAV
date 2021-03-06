# Generated by Django 3.0.4 on 2020-04-27 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
                ('description', models.CharField(max_length=200, verbose_name='Descrição')),
                ('pub_date', models.DateTimeField(verbose_name='Data de Cadastro')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Customer')),
            ],
        ),
    ]
