from django.http import HttpResponse
from django.shortcuts import render, redirect  
from django.conf import settings
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.utils import timezone

from sales.forms import RegisterCustomerForm, RegisterSaleForm
from .models import Customer, Sale


class CustomerList(ListView):
    model = Customer
    template_name = 'customer/listar.html'
    context_object_name = 'customers'


def index(request):
    return HttpResponse("Clientes")


def registerCustomer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.pub_date = timezone.now()
            customer.save()
            return redirect('customer_list')
 
    else:
        form = RegisterCustomerForm()
    context = {
        'form': form
    }
    return render(request, 'customer/cadastrar_cliente.html', {'form' : RegisterCustomerForm()})


def deleteCustomer(request, pk):
    query = Customer.objects.get(pk=pk)
    query.delete()
    return redirect('customer_list')


def updateCustomer(request, pk):
    query = get_object_or_404(Customer, pk=pk)
    form = RegisterCustomerForm(instance=query)

    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST, instance=query)

        if form.is_valid():
            query = form.save(commit= False)
            query.customer_name = form.cleaned_data['customer_name']
            query.customer_reference = form.cleaned_data['customer_reference']
            query.customer_location = form.cleaned_data['customer_location']
            query.customer_phone = form.cleaned_data['customer_phone']
            query.customer_email = form.cleaned_data['customer_email']

            query.save()

            return redirect('customer_list')

    return render(request, 'customer/cadastrar_cliente.html', {'form': form, 'customer': query})


class SaleList(ListView):
    model = Sale
    template_name = 'sale/listar.html'
    context_object_name = 'sales'


def registerSale(request):

    if request.method == 'POST':
        form = RegisterSaleForm(request.POST)
        if form.is_valid():
            query = form.save(commit= False)
            query.customer = form.cleaned_data['customer']
            query.value = form.cleaned_data['value']
            query.pub_date = form.cleaned_data['pub_date']

            query.save()

            return redirect('sale_list')

    else:
        form = RegisterSaleForm()
    context = {
        'form': form
    }
    return render(request, 'sale/cadastrar.html', {'form': RegisterSaleForm()})


def updateSale(request, pk):
    query = Sale.objects.get(pk=pk)
    query.delete()
    return redirect('sale_list')


def deleteSale(request, pk):
    query = Sale.objects.get(pk=pk)
    query.delete()
    return redirect('sale_list')