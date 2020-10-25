# Android Package Uninstaller# Caution!* I'm not responsible for bricked devices, dead SD cards, thermonuclear war, or you getting fired because the alarm app failed (like it did for me...).* YOU are choosing to make these modifications, and if you point the finger at me for messing up your device, I will laugh at you.# FAQ## WhyThis project was done as a research concerning the privacy status in the software that is used by people everyday, developing finally a possible solution to this in Android devices. The solution found needed technical knowledge which not all people may have, and that's why this program was done.It simply uses Android Debug Bridge from Google's _platform-tools_ to:* Let the user know which packages are installed on his device for the default user    * Package path    * Package apk name    * Package name* Filter through a keyword that can be on installation path, apk name or package name* Uninstall for the default user the selected package## OK, but I can already uninstall all the stuff I want from my deviceYes, indeed you can. But you can only uninstall certain applications, not any package you want from the device. To be clear: all applications appear on the device as packages, but not all packages are "like normal apps". Some packages just run in the background without you noticing it. You would be surprised about the amount of packages you device has, so just give it a try and at least find out what's inside your device.# How to use itFirst of all, please ensure you have:* [Developer options enabled](#enable-developer-options)* [Debug mode activated](#activate-debug-mode)After these both are activated, and **ONLY** for the first time, you will need to press `Load packages for device`. This will pop up a window in your device, asking you If you really trust the device trying to connect to the device. Press `yes` If you want to use the program, as this grants the later communications done between the program and the device.Now you can press again `Load packages for device`, and you will see all the packages in your device. You can filter by adding some text in the box and selecting `Filter`, or you can directly scroll up/down to find any package.To uninstall a package, just click on it, see that it appears as selected, and then press `Uninstall package from device`.Now you won't see that package installed in your device anymore.# Steps to reproduce development environment**NOTE: You need to install Python 3.8 or newer**You can simply download the project and execute it to have it running. On the file `requirements.txt` you can find the needed packages to run the project. As these requirements will be installed, I recommend to use a virtual env. To install them, you just need to:```bashpip install -r requirements.txt```After this, `pip` should have successfully installed all the necessary packages. Following this, you will also need to install the main project folder as a package, as it uses different modules and it was needed to properly define imports having a main module defined. To do so, you will need to:```bashpip install -e .```Finally, for running the project, you should just run:```bashpython main.py```# Creating standalone app for your environment**NOTE: First of all, you need to reproduce the [development environment](#steps-to-reproduce-development-environment)**You need to install `Python 3.8` or newer along with `pyinstaller`. This will create a standalone app just for the environment you use to do this. E.g If you do this from a Windows machine, you will create a standalone for Windows devices.Once you have the development environment prepared and `pyinstaller` installed, just type:```bashpyinstaller -F main.py```This will create a new directory named `/dist` with a file named `main` will appear. For Windows devices, you will see the `.exe` extension, while doing this from macOs or linux devices, it will create the corresponding executable file.# Other actionsYou may need to do the following before getting your hands dirty. All the modifications are done by you, under your own risks. These shouldn't harm your device though...## Enable Developer OptionsTo enable our device's developer options we just need to get into system settings and go to software information. Inside this window, we have to search for the build number, and keep touching it until a toast appears saying that `developer options have been granted`.## Activate Debug Mode**NOTE: You MUST have enabled `Developer Options` to access this feature**Just navigate to `Developer Options` section and search for `USB debugging` option and activate it.## Give execution rights to the application`Work In Progress`# ThanksAll the knowledge required to do this project has been acquired reading different posts from XDA, reddit and other internet resources like Google's documentation. Thanks to all users that collaborate, help and write in different forums helping people, without you this would have never been possible.