from django.urls import path

from payments.views import PaymentListCreateView, PaymentDetailView

payments_router = [
    path('payments', PaymentListCreateView.as_view()),
    path('payments/<str:pk>', PaymentDetailView.as_view()),
]
