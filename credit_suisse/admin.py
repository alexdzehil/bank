from django.contrib import admin

from credit_suisse.models import Product, Producer, LoanApplication, Contract


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_producer', 'created']
    readonly_fields = ['created']


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']
    readonly_fields = ['created']


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ['loan_contract', 'created']
    readonly_fields = ['created']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['contract_id', 'name', 'created']
    readonly_fields = ['created']
