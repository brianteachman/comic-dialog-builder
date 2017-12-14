import tkinter as tk
from tkinter import ttk


class CaptionEditor:
    """ """

    def __init__(self, parent, scene):
        """ Image Dialog Editor """
        self.parent = parent
        editor = ttk.Labelframe(self.parent, text='Scene Editor', padding="3 3 12 12")
        # editor = ttk.Frame(self.parent, padding="3 3 12 12")
        editor.grid(row=2, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        dialog = tk.StringVar()
        ttk.Entry(editor, textvariable=dialog, width=25).grid(row=0, column=0, sticky=(tk.W, tk.E))
        ttk.Separator(self.parent, orient=tk.HORIZONTAL)

        ttk.Button(editor, text="Update", command=scene.update_scene).grid(row=1, column=0, sticky=tk.E)
        ttk.Label(editor, textvariable="Some message").grid(row=1, column=1, sticky=(tk.W, tk.E))
        ttk.Separator(self.parent, orient=tk.HORIZONTAL)

        ttk.Button(self.parent, text="Close", command=self.parent.quit).grid(row=2, column=0, sticky=tk.E)