from django.http import JsonResponse

from credit_suisse.utils import get_unique_ids


def get_producer_unique_ids(request):
    contract_id = request.GET.get('contract_id')
    context = {'unique_ids': list(get_unique_ids(contract_id))}
    return JsonResponse(context)
