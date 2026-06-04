from flask import Flask
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)

    # Secret key for sessions (OK for development)
    app.config['SECRET_KEY'] = 'dev-secret-key'

    # SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Import blueprints
    from auth import auth_bp
    from notes import notes_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    
    app.run(debug=True)
