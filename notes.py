from flask import Blueprint, request
from flask_login import login_required, current_user
from models import Note
from extensions import db
from security.encryption import encrypt, decrypt
from security.logger import log_event

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/note', methods=['POST'])
@login_required
def create_note():
    data = request.json

    encrypted_note = encrypt(data['content'])

    note = Note(
        owner_id=current_user.id,
        encrypted_content=encrypted_note,
        classification=data['classification']
    )

    db.session.add(note)
    db.session.commit()

    log_event("NOTE_CREATED", current_user.id)

    return {"message": "Note saved securely"}


@notes_bp.route('/notes', methods=['GET'])
@login_required
def get_notes():
    notes = Note.query.filter_by(owner_id=current_user.id).all()

    response = []
    for note in notes:
        response.append({
            "content": decrypt(note.encrypted_content),
            "classification": note.classification
        })

    return response
