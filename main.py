from androidpackageuninstaller.infrastructure.task.adb.adb_download import AdbDownload
from androidpackageuninstaller.view.main_view import View


class MainExecution:

    def __init__(self):
        self.__prepare_environment()
        self.__run_view()

    @staticmethod
    def __prepare_environment():
        # Preparamos el entorno ejecutando la tarea de descarga de ADB
        AdbDownload().download_and_extract_adb()

    @staticmethod
    def __run_view():
        # Creamos la ventana principal y la mostramos
        app = View()
        app.mainloop()


if __name__ == '__main__':
    MainExecution()
