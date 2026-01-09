from flask import Blueprint, request
from flask_login import login_user
from models import User
from extensions import db
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    hashed_pw = bcrypt.hashpw(
        data['password'].encode(),
        bcrypt.gensalt()
    )

    user = User(
        email=data['email'],
        password_hash=hashed_pw
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "User registered successfully"}


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.checkpw(
        data['password'].encode(),
        user.password_hash
    ):
        login_user(user)
        return {"message": "Login successful"}

    return {"error": "Invalid credentials"}, 401
