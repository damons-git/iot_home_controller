import abc
from abc import ABC, abstractmethod

from .auth_types import AuthType


class Authentication(ABC):
    """
    Abstract class to define common behaviour
    for authentication types

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, auth_type: AuthType, required: bool):
        self.auth_type = auth_type
        self.required = required