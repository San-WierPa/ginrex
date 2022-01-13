import pyperclip
import PySimpleGUI as sg

# sys.path.insert(0, "C:\\Users\\yuli.pari\\Desktop\\gitUni\\ginRex\\ginrex\\io")
from ginrex.io.readtxt import read_file

# sys.path.insert(0, "C:\\Users\\yuli.pari\\Desktop\\gitUni\\ginRex\\ginrex")
from ginrex.splitter import PySplitter
from ginrex.ui.plot_exafs import absorption
from ginrex.ui.treeElementBtn import browsefiles
from PySimpleGUI.PySimpleGUI import Window


class UITabWindow:
    """
    Class for creating multiple windows.

    Attributes
    ----------
    theme : any
    filename : str

    Methods
    -------
    make_window(theme):
        Handles the layout of the tab-window and returns the window.
    make_tabwdw():
        Handles the event loop.
    """

    def make_window(self, theme) -> Window:
        """
        Defines the layout for the tab-window.

        Parameters
        ----------
        theme: Any

        Returns
        -------
        PySimpleGUI Window.
        """
        sg.set_options(auto_size_buttons=True)
        sg.theme(theme)
        menu_def = [["&Application", ["E&xit"]], ["&Help", ["&About"]]]

        menu_layout = [[sg.Menu(menu_def, key="-MENU-")]]

        loaddata_layout = [
            [
                sg.Button("Open Folder"),
                sg.Button("Open File"),
            ],
        ]
        exafs_layout = [
            [sg.Button("Absorption")],
        ]

        qexafs_layout = [
            [sg.Button("Number of rows")],
        ]
        reflexafs_layout = [
            [sg.Button("Plot Reflexafs Spectrum")],
        ]
        layout = [
            [
                sg.Text(
                    "Home of ginrex",
                    size=(38, 1),
                    justification="center",
                    font=("Helvetica", 16),
                    relief=sg.RELIEF_RIDGE,
                    k="-TEXT HEADING-",
                    enable_events=True,
                )
            ]
        ]

        layout += [
            [
                sg.TabGroup(
                    [
                        [
                            sg.Tab("Load Data", loaddata_layout),
                            sg.Tab("EXAFS", exafs_layout),
                            sg.Tab("QEXAFS", qexafs_layout),
                            sg.Tab("ReflEXAFS", reflexafs_layout),
                            sg.Tab("Input Elements", menu_layout),
                        ]
                    ],
                    key="-TAB GROUP-",
                )
            ]
        ]
        return sg.Window(
            "ginrex",
            layout,
        )

    def make_tabwdw(self) -> None:
        """
        Calculates the absorption according to PetraIII columns I1 and I0
        and plots a simple figure.

        Parameters
        ----------
        filename: String

        Returns
        -------
        Window with multiple tabs and tab-specific buttons.
        """
        window = self.make_window(sg.theme("GreenTan"))

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            elif event == "Open Folder":
                browsefiles()
            elif event == "Open File":
                read_file()
            elif event == "Absorption":
                filename = pyperclip.paste()
                absorption(filename)
            elif event == "Number of rows":
                filename = pyperclip.paste()
                rows = PySplitter.counting_rows(filename)
                sg.Print(rows, do_not_reroute_stdout=False)
        window.close()
