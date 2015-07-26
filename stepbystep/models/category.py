from stepbystep import db
from mongoengine import DENY, NULLIFY
from datetime import datetime


class CategoryModel(db.Document):
    name = db.StringField(max_length=255)
    parent = db.ReferenceField(
        'CategoryModel',
        reverse_delete_rule=DENY
    )
    created_at = db.DateTimeField(
        default = datetime.now,
        required = True
    )

    def __unicode__(self):
        return '%s' % self.name
