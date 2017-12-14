import tkinter as tk
from tkinter import ttk

from PIL import Image


class TopMenu:
    """ Controller class """

    def __init__(self, parent, deps):
        self.parent = parent
        self.deps = deps

        """ Add title bar to Window """
        self.parent.titleBar = ttk.Label(self.parent, text='Menu stuff here...')
        # it's important to add this before creating menu
        self.parent.option_add('*tearOff', tk.FALSE)
        # Without it, each of your menus (on Windows and X11) will start with
        # what looks like a dashed line, and allows you to "tear off" the menu
        # so it appears in its own window.

        menubar = tk.Menu(self.parent)  # This method doesn't create two windows.
        self.parent.config(menu=menubar)

        # -----------------------------------------------------------------------------
        # Top-level menu items
        # -----------------------------------------------------------------------------

        menu_file = tk.Menu(menubar)
        menu_edit = tk.Menu(menubar)
        menu_help = tk.Menu(menubar, name='help')
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Edit')
        menubar.add_cascade(menu=menu_help, label='Help')

        menu_help.add_separator()

        # -----------------------------------------------------------------------------
        # File menu items
        # -----------------------------------------------------------------------------

        # menu_file.add_command(label='New', command=self.file_new)

        menu_file.add_command(label='Open', command=self.file_open)

        if self.deps['canvas']:
            print("Menu loaded scene.")
            menu_file.add_command(label='Save', command=self.deps['canvas'].save_scene)

        menu_file.add_separator()  # ---------------------------------------------------

        menu_file.add_command(label='Quit', command=self.parent.quit)

        # -----------------------------------------------------------------------------
        # Edit menu items
        # -----------------------------------------------------------------------------

        menu_edit.add_command(label='Color Picker', command=self.color_picker)

        # -----------------------------------------------------------------------------
        # Help menu items
        # -----------------------------------------------------------------------------

        menu_help.add_command(label='About ComicDialog', command=self.help)

    def load_dep(self, name, a_dep):
        """ Load services (Service manager) """
        self.deps[name] = a_dep

    # -----------------------------------------------------------------------------
    # File menu callbacks
    # -----------------------------------------------------------------------------

    def file_open(self):
        filename = tk.filedialog.askopenfilename()
        image = self.deps['canvas'].new_image(filename)

        # img = self.deps['canvas'].new_image(str(filename), (600, 400))
        # self.deps['canvas'].load_scene_image(img)
        # self.deps['canvas'].reload_scene_image(filename, image.size)
        # self.deps['canvas'].reload_scene_image(filename, (width, height))
        self.deps['canvas'].reload_scene_image(filename, (600, 400))

        # print(self.deps['canvas'].configure()['width'])
        # self.deps['canvas'].load_scene_image(Image.open(filename))
        print("Opened", filename)
        # filename = tk.filedialog.askdirectory()

    # -----------------------------------------------------------------------------
    # Edit menu callbacks
    # -----------------------------------------------------------------------------

    def color_picker(self):
        color = tk.colorchooser.askcolor(initialcolor='#ff0000')
        print(color)

    # -----------------------------------------------------------------------------
    # Help menu callbacks
    # -----------------------------------------------------------------------------

    def help(self):
        help_dialog = tk.Toplevel(height=400, width=400)
        help_dialog.title('About Comic Dialog Editor 2017.')
        about_text = ttk.Label(help_dialog, text='To Logan, built with love. - Dad :)')
        about_text.grid(row=0, column=0, padx=20, pady=20, sticky=(tk.N, tk.W, tk.E, tk.S))
        help_dialog.focus_force()

