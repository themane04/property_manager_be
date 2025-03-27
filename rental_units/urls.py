from django.urls import path

from rental_units.views import RentalUnitListCreateView, RentalUnitDetailView

rental_units_router = [
    path('rental-units', RentalUnitListCreateView.as_view()),
    path('rental-units/<str:pk>', RentalUnitDetailView.as_view()),
]
