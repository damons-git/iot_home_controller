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


    def create_device(self, device: DeviceType, config: dict) -> Device:
        # Given a device type and a corresponding JSON config
        # create and return an instance of that device type
        if device is DeviceType.TASMOTA:
            return self.__create_tasmota(config)

        elif device is DeviceType.ZIGBEE:
            return self.__create_zigbee(config)

        else:
            self.logger.error("Device type {0} not implemented in device factory".format(device))
            return None


    def __create_tasmota(self, config: dict) -> TasmotaDevice:
        # Instantiate an instance of a Tasmota device
        try:
            ip          = config["connection"]["ip_address"]
            port        = config["connection"]["ip_port"]
            username    = config["authentication"]["username"]
            password    = config["authentication"]["password"]
            commands    = dict([self.__create_tasmota_command(cmnd) for cmnd in config["commands"]])
            requests    = dict([self.__create_tasmota_command(req)  for req  in config["requests"]])

        except KeyError as err:
            self.logger.error("Cannot parse tasmota device as required fields are not present in config: {}".format(config))
            return None

        auth = HttpBasic(AuthType.HTTP_BASIC, True, username, password)
        return TasmotaDevice(
                config["name"],
                config["description"],
                DeviceType.TASMOTA,
                config["active"],
                ip,
                port,
                auth,
                commands,
                requests
            )

    def __create_tasmota_command(self, command_conf: dict):
        # Helper function for creating tasmota commands
        try:
            name    = command_conf["name"]
            desc    = command_conf["description"]
            command = command_conf["command"]
            example = command_conf["example"]
            return (name, TasmotaCommand(name, desc, command, example))

        except:
            self.logger.error("Unable to parse tasmota command: {}".format(command_conf))
            return None


    def __create_zigbee(self, config: dict) -> ZigbeeDevice:
        return NotImplementedError


    def __create_authentication(self, config: dict):
        raise NotImplementedError


    def __create_communication(self, config: dict):
        raise NotImplementedError