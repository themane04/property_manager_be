from rest_framework import routers
from django.urls import path, include
from django.contrib import admin

from features.urls import features_router
from maintenance_request.urls import maintenance_request_router
from payments.urls import payments_router
from properties.urls import properties_router
from rental_contracts.urls import rental_contracts_router
from rental_units.urls import rental_units_router
from tenants.urls import tenants_router

router = routers.SimpleRouter(trailing_slash=False)

api_urlpatterns = [
    path('', include(router.urls)),
    *tenants_router,
    *properties_router,
    *rental_units_router,
    *rental_contracts_router,
    *payments_router,
    *maintenance_request_router,
    *features_router,
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]
