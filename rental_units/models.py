from mongoengine import Document, StringField, IntField, DecimalField, DateField, ReferenceField, ListField

from NewPropertyManager.statics import RENTAL_UNIT_TYPE_CHOICES, RENTAL_UNIT_STATUS_CHOICES
from tenants.models import Tenant
from properties.models import Property
from features.models import Feature


class RentalUnit(Document):
    designation = StringField(required=True, max_length=100)
    type = StringField(required=True, choices=RENTAL_UNIT_TYPE_CHOICES)
    area_m2 = IntField()
    number_of_rooms = IntField()
    rent = DecimalField(precision=2)
    available_from = DateField()
    status = StringField(choices=RENTAL_UNIT_STATUS_CHOICES)
    tenant = ReferenceField(Tenant, null=True)
    properties = ReferenceField(Property, required=True)
    features = ListField(ReferenceField(Feature))
