from credit_suisse.models import LoanApplication


def get_unique_ids(contract_id):
    unique_ids = LoanApplication.objects.filter(
        loan_contract__contract_id=contract_id
    ).values_list('loan_product__product_producer_id', flat=True).distinct()
    return unique_ids
