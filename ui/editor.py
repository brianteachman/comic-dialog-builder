import tkinter as tk
from tkinter import ttk


class CaptionEditor:
    """ """
    caption_text = None

    def __init__(self, parent, scene):
        """ Image Dialog Editor """
        self.parent = parent

        self.caption_text = tk.StringVar()

        # -------------------------------------------------------------------
        # Input Frame
        # -------------------------------------------------------------------

        editor = ttk.Labelframe(self.parent, text='Scene Editor', padding="3 3 12 12")
        # editor = ttk.Frame(self.parent, padding="3 3 12 12")
        editor.grid(row=2, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self._is_caption_locked = False
        captions_lock = ttk.Checkbutton(self.parent, text='Adjust captions', command=self.caption_lock)
        captions_lock.grid(row=0, column=0)

        #  Entry form -------------------------------------------------------

        # MODIFIES: self.caption_text
        caption_entry = ttk.Entry(editor, textvariable=self.caption_text, width=25)
        caption_entry.grid(row=0, column=0, columnspan=2,
                           padx=2, pady=1, ipadx=2, ipady=2,
                           sticky=(tk.N, tk.E, tk.W))

        ttk.Separator(self.parent, orient=tk.HORIZONTAL)

        update_btn = ttk.Button(editor, text="Update", command=self.update_message)
        update_btn.grid(row=1, column=0, padx=2, pady=2, sticky=tk.E)

        ttk.Separator(self.parent, orient=tk.HORIZONTAL)

        #  Rotate ----------------------------------------------------------

        ttk.Separator(self.parent, orient=tk.VERTICAL)

        # update_btn = ttk.Button(editor, text="Rotate CW", command=self.update_message)
        cw_btn = ttk.Button(editor, text="Rotate CW")
        cw_btn.grid(row=0, column=2, padx=2, pady=2, sticky=tk.E)

        ccw_btn = ttk.Button(editor, text="Rotate CCW")
        ccw_btn.grid(row=1, column=2, padx=2, pady=2, sticky=tk.E)

        ttk.Separator(self.parent, orient=tk.HORIZONTAL)

        # -------------------------------------------------------------------
        # Output Frame
        # -------------------------------------------------------------------

        editor_output = ttk.Labelframe(self.parent, text='Scene Output', padding="3 3 12 12")
        editor_output.grid(row=2, column=1, padx=2, pady=2, sticky=(tk.N, tk.W, tk.E, tk.S))

        caption_label = ttk.Label(editor_output, textvariable=self.caption_text)
        caption_label.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky=(tk.N, tk.W, tk.E, tk.S))

        # -------------------------------------------------------------------
        # Exit Button
        # -------------------------------------------------------------------

        close_app = ttk.Button(editor_output, text="Exit", command=self.parent.quit)
        close_app.grid(row=0, column=2, padx=5, pady=2, sticky=tk.E)

    def update_message(self):
        print(self.caption_text.get(), 'rumple')

    def caption_lock(self):
        self._is_caption_locked = not self._is_caption_locked
        print(self._is_caption_locked)
