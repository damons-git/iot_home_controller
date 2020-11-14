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

    def create_device(self, device: DeviceType, config: dict) -> Device:
        # Given a device type and a corresponding JSON config
        # create and return an instance of that device type
        if device is DeviceType.TASMOTA:
            return self.__create_tasmota(config)

        elif device is DeviceType.ZIGBEE:
            return self.__create_zigbee(config)

        else:
            print("Device type {0} not implemented in device factory".format(device))
            return None


    def __create_tasmota(self, config: dict) -> TasmotaDevice:
        # Instantiate an instance of a Tasmota device
        ip          = config["connection"]["ip_address"]
        port        = config["connection"]["ip_port"]
        username    = config["authentication"]["username"]
        password    = config["authentication"]["password"]
        commands    = dict([self.__create_tasmota_command(cmnd) for cmnd in config["commands"]])
        requests    = dict([self.__create_tasmota_command(req)  for req  in config["requests"]])

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
            print("Unable to parse tasmota command: {0}".format(dict))
            return None


    def __create_zigbee(self, config: dict) -> ZigbeeDevice:
        return "[Zigbee device]"


    def __create_authentication(self, config: dict):
        raise NotImplementedError


    def __create_communication(self, config: dict):
        raise NotImplementedError