from flask import Blueprint, request, jsonify
from app.schemas.user_schema import UserCreateSchema, UserLoginSchema
from app.services.auth_service import AuthService


auth_router = Blueprint("auth", __name__)


@auth_router.route("/register", methods=["POST"])
def register():

    data = UserCreateSchema(**request.json)

    user = AuthService.register(data)

    return jsonify({"message": "User created", "id": user.id})


@auth_router.route("/login", methods=["POST"])
def login():

    data = UserLoginSchema(**request.json)

    user = AuthService.login(data)

    return jsonify({"message": "Login successful", "user_id": user.id})