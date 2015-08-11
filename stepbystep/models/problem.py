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
        'collection': 'Problem'
    }

    @staticmethod
    def p_cmp(x, y):
        if x.category.parent.ordinal != y.category.parent.ordinal:
            return x.category.parent.ordinal - y.category.parent.ordinal
        elif x.category.ordinal != y.category.ordinal:
            return x.category.ordinal - y.category.ordinal
        else:
            return x.ordinal - y.ordinal

    def __unicode__(self):
        return '%s: %s' % (self.origin_oj, self.problem_id)
