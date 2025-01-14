import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from PyQt6 import QtGui, QtWidgets, QtCore

from labelme import __appname__
from labelme import __version__
from labelme.utils import newIcon

import qdarktheme




def main():
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    app.setApplicationName(__appname__)
    app.setWindowIcon(newIcon("icon"))
    # create and show splash screen
    splash_pix = QtGui.QPixmap('labelme/icons/splash_screen.png')

    splash = QtWidgets.QSplashScreen(splash_pix)


    # center the splash screen to the original screen size
    try:
        from screeninfo import get_monitors

        original_width = get_monitors()[0].width
        original_heigth = get_monitors()[0].height

        slapsh_width = splash.width()
        splash_height = splash.height()

        splash.move(int((original_width - slapsh_width) / 2), int((original_heigth - splash_height) / 2))
    except Exception as e:
        pass



    splash.show()

    qss = """
    QMenuBar::item {
        padding: 10px;
        margin: 0 5px
    }
    QMenu{
        border-radius: 5px;
    }
    QMenu::item{
        padding: 8px;
        margin: 5px;
        border-radius: 5px;
    }
    QToolTip {
            color: #111111;
            background-color: #EEEEEE;
            }
    QCheckBox{
        margin: 0 7px;
    }
    QComboBox{
        font-size: 10pt;
        font-weight: bold;
    }
    """
    try:
        import yaml
        with open ("labelme/config/default_config.yaml", "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        qdarktheme.setup_theme(theme = config["theme"], default_theme = "dark",  additional_qss=qss)
    except Exception as e:
        print(f"ERROR {e}")

    # create main window
    from labelme.app import MainWindow
    win = MainWindow()
    splash.finish(win)
    win.showMaximized()

    # close splash screen

    win.raise_()
    sys.exit(app.exec())


# this main block is required to generate executable by pyinstaller
if __name__ == "__main__":
    main()