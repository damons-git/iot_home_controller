from enum import Enum


class DeviceType(Enum):
    """
    All supported device types

    @Author: Damon M. Sweeney
    @Version: 09-11-2020
    """

    TASMOTA     = 0
    ZIGBEE      = 1
    CUSTOM_REST = 2

    @staticmethod
    def from_str(name: str):
        # Return the DeviceType enum corresponding to the string
        name = name.upper()

        if name in ("TASMOTA"):
            return DeviceType.TASMOTA

        elif name in ("ZIGBEE"):
            return DeviceType.ZIGBEE

        elif name in ("CUSTOM_REST"):
            return DeviceType.CUSTOM_REST

        else:
            raise NotImplementedError("Device type {0} not implemented".format(name))

