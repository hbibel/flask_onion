from flask import Blueprint, request

from flask_onion.application_services.user_service import UserService


class AuthModule:
    def __init__(self, user_service: UserService) -> None:
        self._blueprint = Blueprint("auth", __name__)
        self._user_service = user_service

        self._blueprint.add_url_rule(
            "/register",
            view_func=self.post_user,
            methods=["POST"],
        )

    @property
    def blueprint(self) -> Blueprint:
        return self._blueprint

    def post_user(self):
        username = request.form["username"]
        password = request.form["password"]
        maybe_error = self._user_service.create_and_insert_user(username, password)

        if maybe_error:
            return maybe_error, 400
        return "OK", 200


# Shorter, alternative implementation for very simple blueprints such as this one:
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
