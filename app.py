from tkinter import *
from tkinter import ttk

from ui.scene import Scene
from ui.topmenu import TopMenu
from ui.editor import CaptionEditor

# -------------------------------------------------------------------
# Main Window
# -------------------------------------------------------------------

root = Tk()
root.title("Image/Text layering test.")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# -------------------------------------------------------------------
# Invariants
# -------------------------------------------------------------------

last_x = None
last_y = None

# init messaging invariant
editor_status = 'Ready'
# editor_status = StringVar()
# editor_status.set('Ready')

# -------------------------------------------------------------------
# Scene
# -------------------------------------------------------------------

container = ttk.Frame(root)
container.grid(column=0, row=0, sticky=(N, W, E, S))

canvas = Scene(container, height=400, width=600)  # is a tk.Canvas instance
canvas.grid(column=0, row=0, sticky=(N, W, E))

# -------------------------------------------------------------------

scene_image = canvas.new_image('imgs/saiyaman.gif', (600, 400))
scene_id = canvas.load_scene_image(scene_image)

caption = ("Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello "
           "Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello"
           )

# caption_1 = canvas.add_caption("Cape does not match my suit", bubble_type='thought')
# caption_1 = canvas.add_caption(caption)
# caption_2 = canvas.add_caption("What the #*@$!", bubble_type='thought')

# -------------------------------------------------------------------
# Menubar
# -------------------------------------------------------------------

deps = {
    'canvas': canvas,
}
menu = TopMenu(root, deps)

# -------------------------------------------------------------------
# Dashboard
# -------------------------------------------------------------------

dashboard = ttk.Frame(root)
# dashboard.config(background="white")
dashboard.grid(column=0, row=1, sticky=(N, W, E, S))

# -----------------------------------------------------------------------------

controls = ttk.Button(dashboard, text='Press me!', command=lambda event: print("Stopped."))
# controls.config(bg="white")
controls.grid(column=0, row=0)

# -----------------------------------------------------------------------------

# Checkbox to lock captions
l1_on = False


def layer_on():
    """ Image layer on flag """
    global l1_on
    l1_on = not l1_on
    print(l1_on)


captions_lock = ttk.Checkbutton(dashboard, text='Adjust captions', command=layer_on)
captions_lock.grid(column=1, row=0)

editor = CaptionEditor(dashboard, canvas)
editor.message.set(editor_status)
print(editor.message.get())

# -------------------------------------------------------------------
# Run client
# -------------------------------------------------------------------

caption_1 = canvas.add_caption(editor.message.get())

root.mainloop()
