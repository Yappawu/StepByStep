from stepbystep import db
from mongoengine import DENY, NULLIFY
from datetime import datetime
from .problem import ProblemModel

class CategoryModel(db.Document):
    name = db.StringField(max_length=255)
    children = db.ListField(
        db.ReferenceField(
            'CategoryModel',
            reverse_delete_rule = NULLIFY
        ),
        default=[],
    )
    problems = db.ListField(
        db.ReferenceField(
            'ProblemModel',
            reverse_delete_rule = NULLIFY
        ),
        default=[]
    )
    created_at = db.DateTimeField(
        default = datetime.now,
        required = True
    )

    def __unicode__(self):
        return '%s' % self.name
