from androidpackageuninstaller.infrastructure.task.adb.adb_download import AdbDownload
from androidpackageuninstaller.infrastructure.port.controller import Controller


class MainExecution:

    def __init__(self):
        print('main exec')
        self.get_device_installed_packages()

    @staticmethod
    def prepare_environment():
        AdbDownload().download_and_extract_adb()

    @staticmethod
    def get_device_installed_packages():
        Controller().get_service_list()


if __name__ == '__main__':
    MainExecution()
