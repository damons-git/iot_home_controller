import os
import json

from logger import Logger
from .device_types import DeviceType
from .device import Device
from .tasmota_device import TasmotaDevice
from .zigbee_device import ZigbeeDevice
from .device_factory import DeviceFactory, MalformedDeviceConfig, DeviceNotSupported


class DeviceParser:
    """
    Parse directory of device .json

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, directory: str):
        self.logger = Logger()
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
            self.logger.error("Unable to open config file {0} with error: {1}".format(config_path, err))
            return

        try:
            device_conf = json.loads(config)
            device_type = DeviceType.from_str(device_conf["device_type"])
            device = factory.create_device(device_type, device_conf)
            return device

        except DeviceNotSupported as err:
            self.logger.error("Device type not supported in device factory \"{0}\" in \"{1}\"".format(err, config_path))
            return

        except MalformedDeviceConfig as err:
            self.logger.error("Malformed device configuration file \"{0}\": \"{1}\"".format(config_path, err))
            return

        except Exception as err:
            self.logger.error("Unknown exception: \"{0}\"".format(config_path, err))
            return


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