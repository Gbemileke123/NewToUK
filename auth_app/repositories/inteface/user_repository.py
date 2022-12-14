import uuid
from abc import ABCMeta, abstractmethod
from typing import List

from auth_app.dto.user_dto import CreateDto, GetDto, EditDto, Login
from auth_app.models import User


class UserRepository(metaclass=ABCMeta):
    """Abstract class for user data access (repository)"""

    @abstractmethod
    def create(self, user: CreateDto) -> uuid.UUID:
        """Create a user object and returns the id of thr user created if successful"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[GetDto]:
        """List user objects"""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: uuid.UUID) -> GetDto | None:
        """Get User object by Id"""
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email: str) -> GetDto | None:
        """Get User object by email"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: uuid.UUID, updated_user: EditDto) -> uuid.UUID:
        """Edit a user object"""
        raise NotImplementedError

    @abstractmethod
    def check_if_exist(self, email: str) -> bool:
        """Checks if user exists with email"""
        raise NotImplementedError

    @abstractmethod
    def authenticate(self, username: str, password: str) -> Login:
        """Authenticate user and return information if authenticated"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: uuid.UUID):
        """Delete User Object"""
        raise NotImplementedError
