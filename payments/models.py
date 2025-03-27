from mongoengine import Document, ReferenceField, DateField, DecimalField, StringField

from NewPropertyManager.statics import PAYMENT_STATUS_CHOICES, PAYMENT_METHOD_CHOICES
from rental_contracts.models import RentalContract


class Payment(Document):
    rental_contract = ReferenceField(RentalContract, required=True)
    date = DateField()
    amount = DecimalField(precision=2)
    status = StringField(choices=PAYMENT_STATUS_CHOICES)
    payment_method = StringField(choices=PAYMENT_METHOD_CHOICES)
