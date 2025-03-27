from mongoengine import Document, StringField, DateField


class Tenant(Document):
    first_name = StringField(required=True, max_length=100)
    last_name = StringField(required=True, max_length=100)
    birthday = DateField(required=True)
    email = StringField(required=True)
    phone_number = StringField()
    street = StringField()
    house_number = StringField()
    postal_code = StringField()
    city = StringField()
