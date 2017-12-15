import tkinter as tk
from tkinter import ttk

from ui.editor import CaptionEditor
from ui.scene import Scene
from ui.topmenu import TopMenu


class App:
    """ """
    ITEM_PADDING = 2
    window = {}

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Comic Dialog Editor")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.window['container'] = ttk.Frame(self.root)
        self.window['container'].grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.canvas_width = 600
        self.canvas_height = 400
        self.window['canvas'] = Scene(self.window['container'],
                                      height=self.canvas_height, width=self.canvas_width)
        self.window['canvas'].grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))

        # -------------------------------------------------------------------
        # Menubar
        # -------------------------------------------------------------------

        self.window['menu'] = TopMenu(self.root, self.window)

        # -------------------------------------------------------------------
        # Dashboard
        # -------------------------------------------------------------------

        self.window['dashboard'] = ttk.Frame(self.root)
        self.window['dashboard'].grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))

        # -----------------------------------------------------------------------------

        # Checkbox to lock captions
        # self.l1_on = False

        # -----------------------------------------------------------------------------

        self.window['editor'] = CaptionEditor(self.window['dashboard'], self.window['canvas'])

    def load_scene(self, filename, resize=None):
        if not resize:
            resize = (self.canvas_width, self.canvas_height)
        scene_id = self.window['canvas'].load_scene(filename, resize)

    def add_caption(self, caption):
        if len(caption) < 25:  # trivial, will want to override
            caption_id = self.window['canvas'].add_caption("What the #*@$!", 'thought')
        else:
            caption_id = self.window['canvas'].add_caption(caption)
        self.window['canvas'].captions[caption_id / 2] = caption  # local caption id
        print('Caption', caption_id, 'added')

    def run(self):
        self.root.mainloop()

    def btn_pushed(self):
        print("Button pushed")