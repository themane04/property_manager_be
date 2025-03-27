from django.urls import path

from tenants.views import TenantListCreateView, TenantDetailView

tenants_router = [
    path('tenants', TenantListCreateView.as_view()),
    path('tenants/<str:pk>', TenantDetailView.as_view()),
]
