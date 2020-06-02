from abc import ABCMeta, abstractmethod


class AndroidPackages(metaclass=ABCMeta):

    @abstractmethod
    def get_package_information(self):
        pass

    @abstractmethod
    def get_package_list(self):
        pass

    @abstractmethod
    def uninstall_package(self):
        pass
