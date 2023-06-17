from django.urls import path

from credit_suisse.views import get_producer_unique_ids


app_name = 'credit_suisse'

urlpatterns = [
    path('', get_producer_unique_ids, name='producers'),
]
