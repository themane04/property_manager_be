from django.urls import path

from properties.views import PropertyListCreateView, PropertyDetailView

properties_router = [
    path('properties', PropertyListCreateView.as_view()),
    path('properties/<str:pk>', PropertyDetailView.as_view()),
]
