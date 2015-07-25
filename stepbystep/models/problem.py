from stepbystep import db
from datetime import datetime

class ProblemModel(db.Document):
    origin_oj = db.StringField()
    problem_id = db.StringField()
    created_at = db.DateTimeField(
        default = datetime.now,
        required = True
    )
