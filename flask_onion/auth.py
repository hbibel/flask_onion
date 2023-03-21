from flask import Blueprint, request
from werkzeug.security import generate_password_hash

from flask_onion.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    db = get_db()
    error = None

    if not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."

    if error is None:
        try:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            error = f"User {username} is already registered."
        else:
            return "OK", 200

    return error, 400
