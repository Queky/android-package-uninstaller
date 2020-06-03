from abc import ABCMeta, abstractmethod
from typing import List


class AdbAccessor(metaclass=ABCMeta):

    @abstractmethod
    def get_package_information(self, package_name: str):
        pass

    @abstractmethod
    def get_package_list(self) -> List[str]:
        pass

    @abstractmethod
    def uninstall_package(self, package_name: str):
        pass
