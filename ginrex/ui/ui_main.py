"""
This module starts and maintains the main user interface.
"""

import sys

import PySimpleGUI as sg
from ginrex.ui.firstwindow import make_firstWdw
from ginrex.ui.tabgroup import UI_TabWindow
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow, UI_TabWindow):
    """
    Delegates all imported window-methods.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main()
        self.make_tabwdw()

    def main(self):
        st_wdw = make_firstWdw()
        st_wdw.read()
        st_wdw.close()
        sg.theme("GreenTan")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.close()
