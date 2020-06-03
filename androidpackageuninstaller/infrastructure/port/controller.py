from androidpackageuninstaller.application.usecase.getpackageinformation.get_package_information \
    import GetPackageInformation
from androidpackageuninstaller.application.usecase.getpackageinformation.get_package_information_command \
    import GetServiceInformationCommand
from androidpackageuninstaller.application.usecase.getpackagelist.get_package_list import GetPackageList
from androidpackageuninstaller.application.usecase.uninstallpackage.uninstall_package import UninstallPackage
from androidpackageuninstaller.application.usecase.uninstallpackage.uninstall_package_command \
    import UninstallServiceCommand


class Controller:

    def get_package_information(self=None):
        service_info = GetPackageInformation()
        service_info.execute(self.__build_get_package_information_command())

    @staticmethod
    def get_package_list():
        print('controller')
        service_list = GetPackageList()
        service_list.execute()

    def uninstall_package(self=None):
        uninstall_service = UninstallPackage()
        uninstall_service.execute(self.__build_uninstall_service_command())

    @staticmethod
    def __build_get_package_information_command(package_name: str) -> GetServiceInformationCommand:
        return GetServiceInformationCommand(package_name)

    @staticmethod
    def __build_uninstall_service_command() -> UninstallServiceCommand:
        return UninstallServiceCommand()
