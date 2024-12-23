from peewee import Model, CharField,  DateTimeField,ForeignKeyField,IntegerField
from .db import db
from .user import User
from .tag import Tag

class Article(Model):
    title = CharField()
    tag = ForeignKeyField(Tag, backref='tags')
    created_at = DateTimeField()
    
    

    class Meta:
        database = db