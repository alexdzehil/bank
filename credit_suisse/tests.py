from django.test import TestCase
from credit_suisse.models import LoanApplication, Contract, Producer, Product


class GetUniqueIdsTest(TestCase):

    def setUp(self):
        self.contract_id = 32812
        contract = Contract.objects.create(contract_id=self.contract_id)
        adidas = Producer.objects.create(name='adidas')
        nike = Producer.objects.create(name='nike')
        reebok = Producer.objects.create(name='reebok')
        product_1 = Product.objects.create(name='1', product_producer=nike)
        product_2 = Product.objects.create(name='2', product_producer=nike)
        product_3 = Product.objects.create(name='3', product_producer=reebok)
        product_4 = Product.objects.create(name='4', product_producer=reebok)
        product_5 = Product.objects.create(name='5', product_producer=adidas)
        loan_application = LoanApplication.objects.create(loan_contract=contract)
        loan_application.loan_product.add(
            product_1, product_2, product_3, product_4, product_5
        )

    def test_get_unique_ids(self):
        from .views import get_unique_ids
        unique_ids = get_unique_ids(self.contract_id)
        expected_ids = [producer.id for producer in Producer.objects.all()]

        self.assertCountEqual(unique_ids, expected_ids)
