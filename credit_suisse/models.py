import uuid

from django.db import models


class CreatedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class Producer(CreatedMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contract(CreatedMixin):
    contract_id = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(CreatedMixin):
    name = models.CharField(max_length=100)
    product_producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return f'{self.product_producer.name} {self.name}'


class LoanApplication(CreatedMixin):
    loan_contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name='loan'
    )
    loan_product = models.ManyToManyField(
        Product,
        related_name='loan'
    )

    def __str__(self):
        return f'Loan - {self.loan_contract.name}'
