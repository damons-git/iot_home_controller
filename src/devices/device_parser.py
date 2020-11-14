import os
import json

from .device_types import DeviceType
from .device import Device
from .tasmota_device import TasmotaDevice
from .zigbee_device import ZigbeeDevice
from .device_factory import DeviceFactory


class DeviceParser:
    """
    Parse directory of device .json

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, directory: str):
        self.directory = directory
        self.failed = []
        self.succeeded = []


    def load_device(self, config_path: str) -> Device:
        # Parse config and return corresponding device object
        factory = DeviceFactory()

        try:
            handle = open(config_path, 'r')
            config = handle.read()

        except Exception as err:
            print("Unable to open config file {0} with error: {1}".format(config_path, err))

        if self.valid_json(config):
            device_conf = json.loads(config)
            device_type = DeviceType.from_str(device_conf["device_type"])
            device = factory.create_device(device_type, device_conf)
            return device

        else:
            return None


    def get_configs(self) -> [str]:
        # Fetch set of config files in environemnt specified directory
        try:
            files = [self.directory + f for f
                in os.listdir(self.directory)
                if os.path.isfile(self.directory + f)
                and os.path.splitext(f)[1] == '.json']

        except Exception as err:
            print(err)

        return files


    def valid_json(self, value: str) -> bool:
        # Guard to check that string provided is parsable JSON
        try:
            json.loads(value)
            return True

        except ValueError:
            return False

        except Exception as err:
            print(err)
            return False