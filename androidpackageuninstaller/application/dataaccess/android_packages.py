from abc import ABCMeta, abstractmethod


class AndroidPackages(metaclass=ABCMeta):

    @abstractmethod
    def get_service_information(self):
        pass

    @abstractmethod
    def get_services_list(self):
        pass

    @abstractmethod
    def uninstall_service(self):
        pass
