from stepbystep import db
from mongoengine import DENY
from datetime import datetime


class CategoryModel(db.Document):
    name = db.StringField(max_length=255)
    origin_oj = db.StringField(max_length=255)
    parent = db.ReferenceField(
        'CategoryModel',
        reverse_delete_rule=DENY
    )
    ordinal = db.IntField(default=0)
    created_at = db.DateTimeField(
        default=datetime.now,
        required=True
    )

    def __unicode__(self):
        return '%s' % self.name
