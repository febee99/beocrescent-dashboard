from mongoengine import Document, EmbeddedDocument, connect
from mongoengine.fields import (
    DateTimeField,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    StringField,
    DictField,
    IntField,
    URLField,
    BinaryField,
    BooleanField,
    DynamicField,
    FloatField
)

class Table(Document):

    table = IntField()
    state = IntField()
