import tkinter as tk

from PIL import ImageTk

from ui.captioneditor import CaptionEditor
from ui.scene import Scene
from ui.topmenu import TopMenu


class View:
    def __init__(self, root):
        self.parent = root
        self.frame = tk.Frame(root)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.menu = TopMenu(root)

        filename = '../imgs/pico-geta-500x241.gif'
        scene = Scene(root, filename, (500, 241))
        # self.scene = scene.set_scene_bgimage('../imgs/pico-geta-500x241.gif', (500, 241))
        # scene.set_scene_title('Vageta wont be fooled again')
        scene = ImageTk.PhotoImage(scene)

        self.ui = CaptionEditor(root, scene)
        # ui.load_editor(scene)

