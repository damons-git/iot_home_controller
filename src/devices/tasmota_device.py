import abc
import requests
from requests.exceptions import HTTPError

from .device import Device
from .device_types import DeviceType
from .authentication.http_basic_auth import HttpBasic


class TasmotaDevice(Device):
    """
    Tasmota device

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, name: str, description: str, device_type: DeviceType, active: bool, ip: str, port: int, auth: HttpBasic, commands: dict, requests: dict):
        super(TasmotaDevice, self).__init__(name, description, device_type, active)
        self.ip = ip
        self.port = port
        self.auth = auth
        self.commands = commands
        self.requests = requests


    def execute(self, command_str):
        # Execute a command / data request on the device
        # with the specified name
        command_str = command_str.upper()

        if command_str in self.commands:
            self.command(command_str)

        elif command_str in self.requests:
            self.request(command_str)

        else:
            print("Device \"{0}\" has no matching command or request with name: \"{1}\"".format(self.name, command_str))


    def command(self, name: str):
        # Execute a device command
        command_obj = self.commands[name]

        auth_str = self.__get_authentication()
        cmnd_str = command_obj.command
        url = "http://{0}/cm?{2}{3}".format(
            self.ip,
            self.port,
            cmnd_str,
            auth_str
        )

        resp = self.__get_request(url)
        print(resp.text)


    def request(self, name: str):
        # Execute a device data request
        request_obj = self.requests[name]

        auth_str = self.__get_authentication()
        req_str  = request_obj.command
        url = "http://{0}/cm?{2}{3}".format(
            self.ip,
            self.port,
            req_str,
            auth_str
        )

        resp = self.__get_request(url)
        print(resp.text)


    def __get_request(self, url: str) -> str:
        try:
            response = requests.get(url)
            response.raise_for_status()

        except HTTPError as err:
            print("HTTP error: {}".format(err))
            return None

        except Exception as err:
            print("Exception has occurred: {}".format(err))
            return None

        return response


    def __get_authentication(self):
        # Tasmota devices use basic HTTP authentication
        # Credentials are sent in URL due to ESP8266 core compatability
        auth_param = "&user={}&password={}".format(
            self.auth.username,
            self.auth.password
        )
        return auth_param


class TasmotaCommand:
    """
    Tasmota device command data structure

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, name: str, description: str, command: str, example: str):
        self.name           = name
        self.description    = description
        self.command        = command
        self.example        = example