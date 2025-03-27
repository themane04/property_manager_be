from django.urls import path

from maintenance_request.views import MaintenanceRequestListCreateView, MaintenanceRequestDetailView

maintenance_request_router = [
    path('maintenance-requests', MaintenanceRequestListCreateView.as_view()),
    path('maintenance-requests/<str:pk>', MaintenanceRequestDetailView.as_view()),
]
