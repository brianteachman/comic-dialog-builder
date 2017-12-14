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
        # self.window['canvas'] = Scene(self.window['container'], height=self.canvas_height, width=self.canvas_width)  # tk.Canvas instance
        self.window['canvas'] = Scene(self.window['container'], height=self.canvas_height, width=self.canvas_width)  # tk.Canvas instance
        self.window['canvas'].grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E))
        # self.canvas = Scene(self.container, height=400, width=600)  # is a tk.Canvas instance
        # self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E))

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
        self.l1_on = False

        # -----------------------------------------------------------------------------

        self.window['editor'] = CaptionEditor(self.window['dashboard'], self.window['canvas'])

    def test_scene(self):
        scene_id = self.window['canvas'].load_scene('imgs/saiyaman.gif')
        # scene_id = self.window['canvas'].load_scene('imgs/saiyaman.gif', (self.canvas_width, self.canvas_height))

        caption = ("I am the hope of the universe. I am the answer to all living things "
                   "that cry out for peace. I am protector of the innocent. I am the "
                   "light in the darkness. I am truth. Ally to good! Nightmare to you!"
                   )

        caption_1 = self.window['canvas'].add_caption(caption)
        # caption_1 = self.window['canvas'].add_caption("Cape does not match my suit", bubble_type='thought')
        # caption_2 = self.window['canvas'].add_caption("What the #*@$!", bubble_type='thought')

    def run(self):
        self.root.mainloop()

    def layer_on(self, event):
        """ Image layer on flag """
        self.l1_on = not self.l1_on
        print(self.l1_on)

    def btn_pushed(self):
        print("Button pushed")