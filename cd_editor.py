from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Image/Text layering test.")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# -----------------------------------------------------------------------------

container = ttk.Frame(root)
container.grid(column=0, row=0, sticky=(N, W, E, S))

canvas = Canvas(container)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

# Setup canvas bindings -------------------------------------------------------

mouse_x = None
mouse_y = None


def motion(event):
    mouse_x, mouse_y = event.x, event.y
    posx.set('{}'.format(mouse_x))
    posy.set('{}'.format(mouse_y))
    print('{}, {}'.format(mouse_x, mouse_y))


canvas.bind('<1>', motion)
# canvas.bind('<1>', lambda e: canvas.configure(text='Clicked left mouse button'))
# canvas.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))


def create_caption(img, caption):
    # bubble = PhotoImage(file='spb-300x165.png')
    canvas.create_image(0, 0, anchor=NW, image=img)
    canvas.create_text(75, 25, anchor=NW, text=caption, width=200)

# -----------------------------------------------------------------------------


def build_editor():
    container['padding'] = (5, 0)
    # -----------------------------------------------------------------------------
    editor = ttk.Frame(container)
    editor.grid(row=1, column=0, sticky=(N,W,E))
    editor['padding'] = (10, 10)
    editor['borderwidth'] = 2
    editor['relief'] = 'sunken'
    # -----------------------------------------------------------------------------
    global textarea
    textarea = Text(editor, height=5, width=25)
    textarea.grid(row=0, column=0, sticky=(N,E))
    textarea.insert('1.0', 'Enter something...') # '1.0' means "line 1, character 0"

    ttk.Button(editor, text="Update", command=update_caption).grid(row=2, column=0, sticky=E)
    # -----------------------------------------------------------------------------
    pos_label = ttk.Label(editor)
    pos_label.grid(row=0, column=1, sticky=(N, W))
    pos_label['padding'] = (10, 10)

    global posx, posy
    posx = StringVar()
    posy = StringVar()
    label_x = ttk.Label(editor, textvariable=posx).grid(row=0, column=1, sticky=W)
    label_y = ttk.Label(editor, textvariable=posy).grid(row=1, column=1, sticky=W)


def update_caption():
    caption = textarea.get('1.0', 'end')
    create_caption(bubble, caption)


# -----------------------------------------------------------------------------

bubble = PhotoImage(file='../imgs/spb-300x165.png')
caption_text = (
    "Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello "
    "Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello"
)

create_caption(bubble, caption_text)
build_editor()

# -----------------------------------------------------------------------------
root.mainloop()