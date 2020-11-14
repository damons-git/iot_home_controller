from .auth_types import AuthType
from .auth_interface import Authentication
from .http_basic_auth import HttpBasic
from .api_key_auth import ApiKey


class AuthenticationFactory:
    """
    Factory to instantiate different authentication types

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def create_authentication(self, auth: AuthType, config: dict) -> Authentication:
        # Given JSON authentication details create and
        # return a corresponding authentication instance object`
        if auth is AuthType.HTTP_BASIC:
            return self.__create_http_basic(config)

        elif auth is AuthType.API_KEY:
            return self.__create_api_key(config)

        else:
            print("Authentication type {0} not implemented in authentication factory".format(auth))
            return None


    def __create_http_basic(self, config: dict) -> HttpBasic:
        raise NotImplementedError


    def __create_api_key(self, config: dict) -> ApiKey:
        raise NotImplementedError