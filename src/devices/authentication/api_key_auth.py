import abc

from .auth_interface import Authentication
from .auth_types import AuthType


class ApiKey(Authentication):
    """
    API key authentication

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, auth_type: AuthType, required: bool):
        super(ApiKey, self).__init__(auth_type, required)