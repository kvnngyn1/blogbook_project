from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app import login_manager
from datetime import datetime as dt

class Post(db.Model):
    # all columns below with constraints
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        from app.blueprints.auth.models import User

        data = {
            'id': self.id,
            'body': self.body,
            'date_created': self.date_created,
            'user': User.query.get(self.user_id).to_dict()
        }
        return data

    def from_dict(self, data):
        for field in ['body', 'user_id']:
            if field in data:
                setattr(self, field, data[field])

# HASHING AND SALTING

# lucas-hash
# derek-hash

# HASHING
# password = abc123
# translation => er7p98789arhuo8bozufjn2

# SALTING
# real password for password 1 = abc123
# original = er7p98789arhuo8bozufjn2
# salt = 2q480we89b801dfuuoijsriodfuo

# real password for password 2 = abc123
# original = er7p98789arhuo8bozufjn2
# salt = 84yar8h90fd9n80uO2YAH09

# REAL_PASSWORD = ABC123
# salt = 84yar8h90fd9n80uO2YAH09
