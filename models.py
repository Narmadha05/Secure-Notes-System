from flask_login import UserMixin
from datetime import datetime
from extensions import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.LargeBinary, nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    encrypted_content = db.Column(db.LargeBinary)
    classification = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
