from mongoengine import Document, StringField, IntField


class Property(Document):
    name = StringField(required=True, max_length=255)
    street = StringField(max_length=100)
    house_number = StringField(max_length=10)
    postal_code = StringField(max_length=10)
    city = StringField(max_length=100)
    year_of_construction = IntField()
    flats_amount = IntField()
    park_spaces_amount = IntField()
    owner = StringField(max_length=255)
