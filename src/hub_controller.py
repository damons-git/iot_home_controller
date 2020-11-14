import os
import time

from util import raw_string
from devices.device import Device
from devices.device_types import DeviceType
from devices.device_parser import DeviceParser
from devices.device_factory import DeviceFactory
from devices.tasmota_device import TasmotaDevice
from devices.zigbee_device import ZigbeeDevice


class Controller:

    def __init__(self):
        self.start_time = time.time()


    def start(self):
        try:
            path = raw_string(os.getenv("DEVICE_CONFIG_DIR"))
            parser = DeviceParser(path)
            configs = parser.get_configs()
            device = parser.load_device(configs[0])
            device.execute("toggle")

        except Exception as err:
            print(err)


