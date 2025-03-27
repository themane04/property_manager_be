from mongoengine import Document, ReferenceField, DateField, DecimalField, StringField

from NewPropertyManager.statics import RENTAL_CONTRACT_STATUS_CHOICES
from tenants.models import Tenant
from rental_units.models import RentalUnit


class RentalContract(Document):
    tenant = ReferenceField(Tenant, required=True)
    rental_unit = ReferenceField(RentalUnit, required=True)
    start_of_contract = DateField()
    end_of_contract = DateField()
    rent = DecimalField(precision=2)
    deposit = DecimalField(precision=2)
    status = StringField(choices=RENTAL_CONTRACT_STATUS_CHOICES)
