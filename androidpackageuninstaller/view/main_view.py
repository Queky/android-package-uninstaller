from tkinter import Tk, END, N, S, E, W, Grid, CENTER
from tkinter.ttk import Treeview, Frame, Button, Entry, Scrollbar
from functools import partial
from androidpackageuninstaller.domain.android_package import AndroidPackage
from androidpackageuninstaller.infrastructure.port.controller import Controller
from typing import List, Final


class View(Frame):
    selected_item = object()
    android_packages = List[AndroidPackage]
    tree_view: Final[Treeview]
    filter_value: Entry

    def __init__(self):
        main_window = Tk()
        super().__init__(main_window)

        main_window.minsize(640, 360)
        main_window.title("Android Package Uninstaller")

        self.filter_value = Entry(main_window)
        self.filter_value.grid(row=0, column=1)

        filter_button = Button(main_window, text='Filter', command=self.__filter_packages_by_name)
        filter_button.grid(row=0, column=0)

        self.tree_view = Treeview(main_window, columns=('apk', 'package'))
        vsb = Scrollbar(self.tree_view, orient="vertical", command=self.tree_view.yview)
        vsb.place(relx=0.980, rely=0.0, relheight=1.0, relwidth=0.020)
        self.tree_view.configure(yscrollcommand=vsb.set)
        self.tree_view.heading('#0', text='Directory')
        self.tree_view.heading('#1', text='APK name')
        self.tree_view.column('#1', anchor=CENTER)
        self.tree_view.heading('#2', text='Package name')
        self.tree_view.bind("<<TreeviewSelect>>", self.__on_tree_select)
        self.tree_view.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)

        list_packages = Button(main_window, text='Load packages from device', command=partial(self.__get_device_packages))
        list_packages.grid(row=2, column=0)

        uninstall_button = Button(main_window, text='Uninstall package from device',
                                  command=partial(self.__uninstall_device_package))
        uninstall_button.grid(row=2, column=1)

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)

        for x in range(2):
            Grid.columnconfigure(main_window, x, weight=1)

        for y in range(4):
            Grid.rowconfigure(main_window, y, weight=1)

    def __on_tree_select(self, event):
        self.selected_item = self.tree_view.item(self.tree_view.selection())

    def __get_device_packages(self):
        if self.tree_view.get_children():
            self.tree_view.delete(*self.tree_view.get_children())
        self.android_packages: List[AndroidPackage] = Controller().get_package_list()
        self.android_packages.sort(key=lambda package: package.package_name)
        for android_package in self.android_packages:
            self.tree_view.insert('', END, text=android_package.package_directory,
                                  values=(android_package.package_apk, android_package.package_name))
        self.tree_view.update()

    def __uninstall_device_package(self):
        item_to_uninstall: str = self.selected_item.get('values')[1]
        Controller().uninstall_package(item_to_uninstall)

    def __filter_packages_by_name(self):
        any_filter: str = self.filter_value.get()
        if any_filter:
            self.android_packages: List[AndroidPackage] = Controller().get_package_list()
            self.android_packages.sort(key=lambda package: package.package_name)
            if self.tree_view.get_children():
                self.tree_view.delete(*self.tree_view.get_children())
            for android_package in self.android_packages:
                if any_filter in android_package.package_name \
                        or any_filter in android_package.package_directory:
                    self.tree_view.insert('', END, text=android_package.package_directory,
                                          values=(android_package.package_apk, android_package.package_name))
            self.tree_view.update()
