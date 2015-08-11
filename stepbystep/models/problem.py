from stepbystep import db
from datetime import datetime
from mongoengine import DENY


class ProblemModel(db.Document):
    origin_oj = db.StringField(max_length=255)
    problem_id = db.StringField(max_length=255)
    category = db.ReferenceField(
        'CategoryModel',
        reverse_delete_rule=DENY
    )
    genera = db.ReferenceField(
        'CategoryModel',
        reverse_delete_rule=DENY
    )
    ordinal = db.IntField(default=0)
    created_at = db.DateTimeField(
        default=datetime.now,
        required=True
    )

    meta = {
        'ordering': ['ordinal']
    }

    def __unicode__(self):
        return '%s: %s' % (self.origin_oj, self.problem_id)
