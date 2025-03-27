from django.urls import path

from features.views import FeatureListCreateView, FeatureDetailView

features_router = [
    path('features', FeatureListCreateView.as_view()),
    path('features/<str:pk>', FeatureDetailView.as_view()),
]
