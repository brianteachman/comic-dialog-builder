import tkinter as tk
from tkinter import ttk
from PIL import Image

class Caption(ttk.Label):
    """ """
    canvas_height = 150
    canvas_width = 250
    image_speech = 'imgs/spb-300x165.png'
    image_thought = 'imgs/thought.png'
    assets = {}

    def __init__(self, container, caption_text=None):
        tk.Label.__init__(self, root)
        self.canvas = tk.Canvas(container, height=self.canvas_height, width=self.canvas_width)
        # self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        # self.canvas.bind("<B1-Motion>", self.scroll_move)
        self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        # self.canvas.grid(column=0, row=0)

        self.caption_text = ''
        if caption_text:
            self.set_text(caption_text)

    # def __del__(self):
    #     global _caption_id
    #     _caption_id = 0

    ## Bindings /////////////////////////////////////////////////////

    def scroll_start(self, event):
        # if (event.x >  and event.x < ):
        #     print("yep")
        self.canvas.scan_mark(event.x, event.y)
        # self.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        # self.scan_dragto(event.x, event.y, gain=1)

    ## //////////////////////////////////////////////////////////////

    def create_caption(self, caption_text=None, style=None):
        self.set_caption_background(style)
        self.set_caption_text(caption_text)

    def set_caption_text(self, caption_text):
        self.set_text(caption_text)
        self.canvas.create_text(75, 25, anchor=tk.NW, text=self.caption_text, width=200, tags=('captiontxt'))

    def set_caption_background(self, style='speech'):
        if style == 'thought':
            caption_img = self.new_image(self.image_thought)
            caption_img = tk.PhotoImage(file=caption_img)
        else:
            caption_img = tk.PhotoImage(file=self.new_image(self.image_speech))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=caption_img, tags=('captionimg'))

    def new_image(self, filename, resize=None):
        image = Image.open(filename)  # PIL.Image object
        if resize:
            image = image.resize(resize)
        return image

    def set_text(self, caption_text):
        self.caption_text = caption_text

    def get_text(self):
        if not self.caption_text:
            return ''
        return self.caption_text


def left_button_press(self, event):
    # self.canvas.scan_mark(event.x, event.y)
    self.scan_mark(event.x, event.y)


def mouse_move(self, event):
    # self.canvas.scan_dragto(event.x, event.y, gain=1)
    self.scan_dragto(event.x, event.y, gain=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    container = tk.Frame(root, height=400, width=600)
    container.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
    container.bind("<1>", left_button_press)
    container.bind("<B1-Motion>", mouse_move)

    # caption = Caption(container)
    caption = Caption(root)
    caption.create_caption("Ahoy!")
    # caption.bind("<1>", caption.scroll_start)
    # caption.bind("<B1-Motion>", caption.scroll_move)

    root.mainloop()
