from mongoengine import Document, StringField

class Feature(Document):
    name = StringField(required=True, max_length=50)
