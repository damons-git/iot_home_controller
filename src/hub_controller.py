import os
import time
import sys
import asyncio

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
        self.loop = asyncio.get_event_loop()
        self.shutdown_flag = False
        self.logger = Logger()
        self.start_time = time.time()
        self.devices = []

        try:
            path = raw_string(os.getenv("DEVICE_CONFIG_DIR"))
            parser = DeviceParser(path)
            configs = parser.get_configs()

            for config in configs:
                d = parser.load_device(config)
                if d is not None:
                    self.devices.append(d)

            self.logger.info("Sucessfully loaded the following devices: {0}".format(
                [d.name for d in self.devices]
            ))

        except Exception as err:
            self.logger.critical("Failed to parse/load device configs with thrown Exception: {}".format(err))
            sys.exit()


    def start(self):
        self.logger.info("Starting \"IOT Home Controller\" application..")
        self.devices[0].execute("toggle")

        # Load looping tasks
        self.loop.create_task(self.heartbeat())

        # Start infinite application loop
        self.loop.run_forever()


    def stop(self):
        self.shutdown_flag = True
        self.logger.info("Stopping and cleaning up \"IOT Home Controller\"")
        self.loop.stop()


    async def heartbeat(self):
        # Send periodic heartbeat to all devices with 'HEARTBEAT' command
        # TODO: Stalls as execute is not async at present
        while True:
            if self.shutdown_flag:
                break

            for d in self.devices:
                if d.has_command("HEARTBEAT"):
                    d.execute("HEARTBEAT")

        await asyncio.sleep(0)


