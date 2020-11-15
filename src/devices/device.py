import abc
from abc import ABC, abstractmethod

from .device_types import DeviceType


class Device(ABC):
    """
    Abstract class to define common behaviour
    for devices

    @Author: Damon M. Sweeney
    @Version: 14-11-2020
    """

    def __init__(self, name: str, description: str, device_type: DeviceType, active: bool):
        self.name = name
        self.description = description
        self.device_type = device_type
        self.active = active


    @abc.abstractmethod
    def execute(self, command_name: str):
        raise NotImplementedError


    @abc.abstractmethod
    def command(self, name: str):
        raise NotImplementedError


    @abc.abstractmethod
    def request(self, name: str):
        raise NotImplementedError


    @abc.abstractmethod
    def has_command(self, command_name: str):
        raise NotImplementedError