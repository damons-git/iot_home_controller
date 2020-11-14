from enum import Enum


class AuthType(Enum):
    """
    All supported authentication types

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    HTTP_BASIC      = 0
    API_KEY         = 1

    @staticmethod
    def from_str(name: str):
        # Return the DeviceType enum corresponding to the string
        name = name.upper()

        if name in ("HTTP_BASIC"):
            return AuthType.HTTP_BASIC

        elif name in ("API_KEY"):
            return AuthType.API_KEY

        else:
            raise NotImplementedError("Authentication type {0} not implemented".format(name))

