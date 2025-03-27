from django.urls import path

from rental_contracts.views import RentalContractListCreateView, RentalContractDetailView

rental_contracts_router = [
    path('rental-contracts', RentalContractListCreateView.as_view()),
    path('rental-contracts/<str:pk>', RentalContractDetailView.as_view()),
]
