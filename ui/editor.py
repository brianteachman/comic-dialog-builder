import tkinter as tk
from tkinter import ttk


class CaptionEditor:
    """ """
    caption_text = None

    def __init__(self, parent, scene):
        """ Image Dialog Editor """
        self.parent = parent
        self.scene = scene

        self._is_caption_locked = False
        self.caption_text = tk.StringVar()
        self.bubble_type = tk.StringVar()
        self.current_layer = tk.StringVar()

        # -------------------------------------------------------------------
        # Message Line
        # -------------------------------------------------------------------

        message_line = ttk.Frame(self.parent)
        message_line.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        selected_caption_label = ttk.Label(message_line, text='Selected Caption: ')
        selected_caption_label.grid(row=0, column=0, padx=2, sticky=tk.W)

        self.caption_label = ttk.Label(message_line, textvariable=self.scene.active_caption)
        self.caption_label.config(text=self.scene.active_caption)
        self.caption_label.grid(row=0, column=1, columnspan=2,
                                padx=2, pady=2, sticky=(tk.N, tk.W, tk.E, tk.S))

        layer_manager = ttk.Combobox(message_line, textvariable=self.current_layer)
        layer_manager.grid(row=0, column=3, sticky=tk.E)
        # layer_manager.bind('<<ComboboxSelected>>', function)
        layer_manager['values'] = ('Layer 1', 'Layer 2', 'Layer 3')

        # -------------------------------------------------------------------
        # Caption Editor
        # -------------------------------------------------------------------

        editor = ttk.Labelframe(self.parent, text='Caption Editor', padding="3 3 12 12")
        # editor = ttk.Frame(self.parent, padding="3 3 12 12")
        editor.grid(row=2, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        add_caption_btn = ttk.Button(editor, text="+", width=3)
        add_caption_btn.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)

        del_caption_btn = ttk.Button(editor, text="-", width=3)
        del_caption_btn.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)

        s1 = ttk.Separator(editor, orient=tk.VERTICAL)

        # MODIFIES: self._is_caption_locked
        captions_lock = ttk.Checkbutton(editor, text='Adjust captions', command=self.caption_lock)
        captions_lock.grid(row=0, column=1, sticky=tk.W)
        captions_lock.focus_force()

        #  Entry form -------------------------------------------------------

        # MODIFIES: self.caption_text
        caption_entry = ttk.Entry(editor, textvariable=self.caption_text, width=25)
        caption_entry.grid(row=1, column=1, columnspan=2,
                           padx=2, pady=1, ipadx=2, ipady=2,
                           sticky=(tk.N, tk.E, tk.W))

        ttk.Separator(self.parent, orient=tk.HORIZONTAL)

        #  Set bubble type -------------------------------------------------

        ttk.Separator(editor, orient=tk.VERTICAL)

        # MODIFIES: self.bubble_type
        type_box1 = ttk.Radiobutton(editor, text='Speech', variable=self.bubble_type, value='speech')
        type_box1.grid(row=0, column=3, padx=2, pady=2, sticky=tk.W)
        type_box2 = ttk.Radiobutton(editor, text='Thought', variable=self.bubble_type, value='thought')
        type_box2.grid(row=1, column=3, padx=2, pady=2, sticky=tk.W)
        self.bubble_type.set('speech')  # set default

        ttk.Separator(editor, orient=tk.VERTICAL)

        #  Rotate ----------------------------------------------------------

        # update_btn = ttk.Button(editor, text="Rotate CW", command=self.update_caption)
        cw_btn = ttk.Button(editor, text="Rotate CW")
        cw_btn.grid(row=0, column=4, padx=2, pady=2, sticky=tk.E)

        ccw_btn = ttk.Button(editor, text="Rotate CCW")
        ccw_btn.grid(row=1, column=4, padx=2, pady=2, sticky=tk.E)

        ttk.Separator(self.parent, orient=tk.HORIZONTAL)

        # -------------------------------------------------------------------
        # Output Frame
        # -------------------------------------------------------------------

        editor_output = ttk.Labelframe(self.parent, text='Scene Output', padding="3 3 12 12")
        editor_output.grid(row=2, column=1, padx=2, pady=2, sticky=(tk.N, tk.W, tk.E, tk.S))

        #  Buttons ----------------------------------------------------------

        update_btn = ttk.Button(editor_output, text="Update", command=self.update_caption)
        update_btn.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)

        save_btn = ttk.Button(editor_output, text="Save", command=self.scene.save_scene)
        save_btn.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)

        ttk.Separator(editor_output, orient=tk.HORIZONTAL)

        exit_btn = ttk.Button(self.parent, text="Exit", command=self.parent.quit)
        exit_btn.grid(row=2, column=3, padx=2, pady=2, sticky=tk.E)

    def update_caption(self):
        self.scene.update_caption_text(self.caption_text)
        self.caption_label.config(text=self.scene.active_caption)
        print(self.caption_text.get(), 'rumple')

    def caption_lock(self):
        self._is_caption_locked = not self._is_caption_locked
        print(self._is_caption_locked)
