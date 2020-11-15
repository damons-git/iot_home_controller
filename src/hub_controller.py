import os
import time

from util import raw_string
from logger import Logger
from devices.device import Device
from devices.device_types import DeviceType
from devices.device_parser import DeviceParser
from devices.device_factory import DeviceFactory
from devices.tasmota_device import TasmotaDevice
from devices.zigbee_device import ZigbeeDevice


class Controller:

    def __init__(self):
        self.logger = Logger()
        self.start_time = time.time()


    def start(self):
        try:
            path = raw_string(os.getenv("DEVICE_CONFIG_DIR"))
            parser = DeviceParser(path)
            configs = parser.get_configs()

            devices = []
            for config in configs:
                d = parser.load_device(config)
                devices.append(d)

            devices[0].execute("toggle")

        except Exception as err:
            self.logger.error("Failed to parse device configs with thrown Exception: {}".format(err))


