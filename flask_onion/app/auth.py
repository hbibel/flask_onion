from typing import Annotated

from fastapi import APIRouter, Depends, Form, Response

from flask_onion.app.services import get_user_service
from flask_onion.application_services.user_service import UserService

router = APIRouter()


@router.post("/register")
def post_user(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    user_service: Annotated[UserService, Depends(get_user_service)],
    response: Response,
):
    maybe_error = user_service.create_and_insert_user(username, password)

    if maybe_error:
        response.status_code = 400
        return maybe_error
    return "OK"
