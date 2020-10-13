import os
import sys
import shutil
import subprocess
from typing import Final
from zipfile import ZipFile
from requests import Response, get


class AdbDownload:

    DOWNLOAD_DIRECTORY: Final[str] = os.getcwd() + '/adb'
    PLATFORM_TOOLS_DIRECTORY: Final[str] = DOWNLOAD_DIRECTORY + '/platform-tools'
    MODIFY_OWNER: bool = False

    LINUX_DOWNLOAD_URL: Final[str] = 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip'
    DARWIN_DOWNLOAD_URL: Final[str] = 'https://dl.google.com/android/repository/platform-tools-latest-darwin.zip'
    WINDOWS_DOWNLOAD_URL: Final[str] = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'

    def download_and_extract_adb(self):
        try:
            if not self.has_platform_tools_downloaded():
                self.__create_download_directory(self.DOWNLOAD_DIRECTORY)
                environment = self.__get_environment()
                file_name = self.DOWNLOAD_DIRECTORY + '/' + environment + '.zip'
                self.__download_file(self.__get_download_url(environment), file_name)
                self.__unzip_downloaded_file(self, file_name, self.DOWNLOAD_DIRECTORY)
                self.__modify_owner()
                self.__remove_downloaded_file(file_name)
        except FileExistsError:
            self.__remove_download_directory(self.DOWNLOAD_DIRECTORY)
            self.download_and_extract_adb()

    def __download_file(self, download_link: str, file_name: str):
        response: Response = get(download_link)
        self.__save_downloaded_content(response, file_name)

    def __get_download_url(self, environment: str) -> str:
        # Obtenemos la URL de descarga dependiendo del entorno
        if environment == "linux" or environment == "linux2":
            self.MODIFY_OWNER = True
            return self.LINUX_DOWNLOAD_URL
        elif environment == "darwin":
            self.MODIFY_OWNER = True
            return self.DARWIN_DOWNLOAD_URL
        elif environment == "win32":
            return self.WINDOWS_DOWNLOAD_URL
        else:
            raise ValueError('Provided environment doesnt have any download URL.')

    def has_platform_tools_downloaded(self) -> bool:
        return os.path.isdir(self.DOWNLOAD_DIRECTORY) and os.path.isdir(self.PLATFORM_TOOLS_DIRECTORY)

    @staticmethod
    def __save_downloaded_content(response: Response, file_name: str):
        with open(file_name, 'wb') as file:
            file.write(response.content)

    @staticmethod
    def __unzip_downloaded_file(self, file_name: str, extract_directory: str):
        # Descomprimimos el archivo descargado
        file = ZipFile(file_name)
        file.extractall(extract_directory)
        file.close()

    @staticmethod
    def __get_environment() -> str:
        return sys.platform

    @staticmethod
    def __create_download_directory(directory: str):
        # Creamos la carpeta donde descargar los archivos
        os.makedirs(directory)

    @staticmethod
    def __remove_downloaded_file(file_directory: str):
        # Eliminamos el archivo descargado
        os.remove(file_directory)

    @staticmethod
    def __remove_download_directory(directory: str):
        shutil.rmtree(directory)

    def __modify_owner(self):
        if self.MODIFY_OWNER:
            subprocess.call(['chmod', '-R', '0777', self.DOWNLOAD_DIRECTORY])

