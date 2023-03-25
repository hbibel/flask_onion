from flask import Blueprint, request

from flask_onion.application_services.user_service import UserService


def create_auth_blueprint(user_service: UserService) -> Blueprint:
    auth_blueprint = Blueprint("auth", __name__)

    @auth_blueprint.route("/register", methods=["POST"])
    def post_user():
        username = request.form["username"]
        password = request.form["password"]
        maybe_error = user_service.create_and_insert_user(username, password)

        if maybe_error:
            return maybe_error, 400
        return "OK", 200

    return auth_blueprint
