import abc

from .device import Device
from .device_types import DeviceType


class ZigbeeDevice(Device):
    """
    ZigBee device

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, name: str, description: str, device_type: DeviceType, active: bool):
        super(ZigbeeDevice, self).__init__(name, description, device_type, active)


    def execute(self, command_name: str):
        raise NotImplementedError


    def command(self, name: str):
        raise NotImplementedError


    def request(self, name: str):
        raise NotImplementedError