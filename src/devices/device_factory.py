from logger import Logger
from .device_types import DeviceType
from .device import Device
from .tasmota_device import TasmotaDevice, TasmotaCommand
from .zigbee_device import ZigbeeDevice
from .authentication.http_basic_auth import HttpBasic
from .authentication.auth_types import AuthType


class DeviceFactory:
    """
    Factory to instantiate different device types

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self):
        self.logger = Logger()


    def create_device(self, config_path: str, device: DeviceType, config: dict) -> Device:
        # Given a device type and a corresponding JSON config
        # create and return an instance of that device type
        if device is DeviceType.TASMOTA:
            return self.__create_tasmota(config_path, config)

        elif device is DeviceType.ZIGBEE:
            return self.__create_zigbee(config_path, config)

        else:
            raise DeviceNotSupported(device)
            self.logger.error("Device type {0} not implemented in device factory".format(device))


    def __create_tasmota(self, config_path: str, config: dict) -> TasmotaDevice:
        # Instantiate an instance of a Tasmota device
        try:
            name        = config["name"]
            description = config["description"]
            active      = config["active"]
            ip          = config["connection"]["ip_address"]
            port        = config["connection"]["ip_port"]
            username    = config["authentication"]["username"]
            password    = config["authentication"]["password"]
            commands    = dict([self.__create_tasmota_command(config_path, cmnd) for cmnd in config["commands"]])
            requests    = dict([self.__create_tasmota_command(config_path, req)  for req  in config["requests"]])

        except KeyError as err:
            raise MalformedDeviceConfig(err)

        auth = HttpBasic(AuthType.HTTP_BASIC, True, username, password)
        return TasmotaDevice(
                name,
                description,
                DeviceType.TASMOTA,
                active,
                ip,
                port,
                auth,
                commands,
                requests
            )

    def __create_tasmota_command(self, config_path: str, command_conf: dict):
        # Helper function for creating tasmota commands
        try:
            name    = command_conf["name"]
            desc    = command_conf["description"]
            command = command_conf["command"]
            example = command_conf["example"]
            return (name, TasmotaCommand(name, desc, command, example))

        except:
            self.logger.error("Unable to parse tasmota command for \"{0}\", skipping command: {1}".format(config_path, command_conf))
            return (None, None)


    def __create_zigbee(self, config_path: str, config: dict) -> ZigbeeDevice:
        return NotImplementedError



class DeviceNotSupported(Exception):
    def __init__(self, device_type: DeviceType):
        self.device_type = device_type

    def __repr__(self):
        return "DeviceNotSupported(type: {0})".format(self.device_type)

    def __str__(self):
        return self.__repr__()


class MalformedDeviceConfig(Exception):
    def __init__(self, key: str):
        self.key = key

    def __repr__(self):
        return "MalformedDeviceConfig(key: {0})".format(self.key)

    def __str__(self):
        return self.__repr__()