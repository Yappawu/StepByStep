from stepbystep import db
from datetime import datetime


class ProblemModel(db.Document):
    origin_oj = db.StringField(max_length=255)
    problem_id = db.StringField(max_length=255)
    created_at = db.DateTimeField(
        default=datetime.now,
        required=True
    )

    def __unicode__(self):
        return '%s: %s' % (self.origin_oj, self.problem_id)
