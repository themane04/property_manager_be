from mongoengine import Document, ReferenceField, StringField, DateField

from NewPropertyManager.statics import MAINTENANCE_REQUEST_STATUS_CHOICES
from rental_units.models import RentalUnit


class MaintenanceRequest(Document):
    rental_unit = ReferenceField(RentalUnit, required=True)
    description = StringField()
    status = StringField(choices=MAINTENANCE_REQUEST_STATUS_CHOICES)
    created_at = DateField()
    assigned_craftsman = StringField(max_length=255)
