from django.conf import settings
from django.db import models
from django.template.defaultfilters import floatformat
from django.utils import timezone
import datetime


class Customer (models.Model):
    customer_name = models.CharField('Nome', max_length=200)
    customer_location = models.CharField('Endereço', max_length=200, blank=True)
    customer_reference = models.CharField('Referência', max_length=200, blank=True)
    customer_email = models.EmailField('Email', max_length=200, blank=True)
    customer_phone = models.CharField('Telefone', max_length=200, blank=True)
    pub_date = models.DateTimeField('Data de Cadastro')

    def __str__(self):
        return self.customer_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Sale (models.Model):
    value = models.DecimalField('Valor', max_digits=5, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField('Descrição', max_length=200)
    pub_date = models.DateTimeField('Data de Cadastro')

    def __str__(self):
        return self.value

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
