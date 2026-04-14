from app.exceptions.custom_exceptions import UserAlreadyExists
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.models.user import User


class AuthService:

    @staticmethod
    def register(data):

        user = User(
            username=data.username,
            email=data.email
        )

        user.set_password(data.password)

        return UserRepository.create_user(user)


    @staticmethod
    def login(data):

        user = UserRepository.get_by_email(data.email)

        if not user or not user.check_password(data.password):
            raise UserAlreadyExists("Invalid credentials")

        return user