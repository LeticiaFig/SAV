from django.urls import path

from . import views
from .views import CustomerList, SaleList

urlpatterns = [
    path('customer/', CustomerList.as_view(), name='customer_list'),
    path('customer/cadastrar/', views.registerCustomer, name='register_customer'),
    path('customer/delete/<int:pk>', views.deleteCustomer, name='delete_customer'),
    path('customer/update/<int:pk>', views.updateCustomer, name='update_customer'),

    path('sale/cadastrar/', views.registerSale, name='register_sale'),
    path('sale/delete/<int:pk>', views.deleteSale, name='delete_sale'),
    path('sale/update/<int:pk>', views.updateSale, name='update_sale'),
    path('sale/listar', SaleList.as_view(), name='sale_list'),

]