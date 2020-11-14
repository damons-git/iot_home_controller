import abc

from .auth_interface import Authentication
from .auth_types import AuthType


class HttpBasic(Authentication):
    """
    HTTP basic authentication data structure

    HTTP basic authentication uses a username/password pair to
    authenticate the user.

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, auth_type: AuthType, required: bool, username: str, password: str):
        super(HttpBasic, self).__init__(auth_type, required)
        self.username = username
        self.password = password