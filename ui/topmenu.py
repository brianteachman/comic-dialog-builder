from tkinter import ttk, Menu, FALSE

from ui.scene import Scene


class TopMenu:
    """ Controller class """

    def __init__(self, parent):
        self.parent = parent

        """ Add title bar to Window """
        self.parent.titleBar = ttk.Label(self.parent, text='Menu stuff here...')
        # it's important to add this before creating menu
        self.parent.option_add('*tearOff', FALSE)
        # Without it, each of your menus (on Windows and X11) will start with
        # what looks like a dashed line, and allows you to "tear off" the menu
        # so it appears in its own window.

        menubar = Menu(self.parent)  # This method doesn't create two windows.
        self.parent.config(menu=menubar)

        # -----------------------------------------------------------------------------
        # Top-level menu items
        # -----------------------------------------------------------------------------

        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menu_help = Menu(menubar, name='help')
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Edit')
        menubar.add_cascade(menu=menu_help, label='Help')

        menu_help.add_separator()

        # -----------------------------------------------------------------------------
        # File menu items
        # -----------------------------------------------------------------------------

        scene = Scene(self.parent)
        # menu_file.add_command(label='New', command=newFile)
        # menu_file.add_command(label='Open...', command=openFile)
        menu_file.add_command(label='Save', command=scene.save_scene)
        # menu_file.add_command(label='Close', command=closeFile)

        # menu_file.add_separator()  # ---------------------------------------------------

        menu_file.add_command(label='Quit', command=self.parent.quit)

        # -----------------------------------------------------------------------------
        # Edit menu items
        # -----------------------------------------------------------------------------

        # -----------------------------------------------------------------------------
        # Help menu items
        # -----------------------------------------------------------------------------

        menu_help.add_command(label='About ComicDialog')

