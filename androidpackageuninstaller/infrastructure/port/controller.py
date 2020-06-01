from androidpackageuninstaller.application.usecase.getpackageinformation.get_package_information \
    import GetServiceInformation
from androidpackageuninstaller.application.usecase.getpackageinformation.get_package_information_command \
    import GetServiceInformationCommand
from androidpackageuninstaller.application.usecase.getservicelist.get_package_list import GetServiceList
from androidpackageuninstaller.application.usecase.getservicelist.get_package_list_command import GetServiceListCommand
from androidpackageuninstaller.application.usecase.uninstallservice.uninstall_package import UninstallService
from androidpackageuninstaller.application.usecase.uninstallservice.uninstall_package_command \
    import UninstallServiceCommand


class Controller:

    def get_service_information(self=None):
        service_info = GetServiceInformation()
        service_info.execute(self.__build_get_service_information_command())

    def get_service_list(self=None):
        print('controller')
        service_list = GetServiceList()
        service_list.execute(self.__build_get_service_list_command())

    def uninstall_service(self=None):
        uninstall_service = UninstallService()
        uninstall_service.execute(self.__build_uninstall_service_command())

    @staticmethod
    def __build_get_service_information_command() -> GetServiceInformationCommand:
        return GetServiceInformationCommand()

    @staticmethod
    def __build_get_service_list_command() -> GetServiceListCommand:
        return GetServiceListCommand()

    @staticmethod
    def __build_uninstall_service_command() -> UninstallServiceCommand:
        return UninstallServiceCommand()
