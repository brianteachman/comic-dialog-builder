import tkinter as tk
from tkinter import ttk

_caption_id = 0 # unique caption id


# class Caption(tk.Frame):
class CanvasCaption(tk.Canvas):
    """ """
    canvas_height = 150
    canvas_width = 250
    image_speech = 'imgs/spb-300x165.png'
    image_thought = 'imgs/thought.png'
    assets = {}

    def __init__(self, container, caption_text=None):
        tk.Canvas.__init__(self, root, height=self.canvas_height, width=self.canvas_width)

        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        global _caption_id
        self.cid = _caption_id + 1

        self.bind("<ButtonPress-1>", self.scroll_start)
        self.bind("<B1-Motion>", self.scroll_move)


        self.caption_text = ''
        if caption_text:
            self.set_text(caption_text)

    # def __del__(self):
    #     global _caption_id
    #     _caption_id = 0

    def scroll_start(self, event):
        # if (event.x >  and event.x < ):
        #     print("yep")
        self.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.scan_dragto(event.x, event.y, gain=1)

    def override_id(self, caption_id):
        global _caption_id
        # floating_id = _caption_id ## if Caption exists move to valid id
        _caption_id = caption_id
        self.cid = caption_id

    def get_id(self):
        return self.cid

    def create_caption(self, caption_text=None, style=None):
        self.set_caption_background(style)
        self.set_caption_text(caption_text)

    def set_caption_text(self, caption_text):
        self.set_text(caption_text)
        self.create_text(75, 25, anchor=tk.NW, text=self.caption_text, width=200, tags=('captiontxt'))

    def set_caption_background(self, style='speech'):
        if style == 'thought':
            caption_img = tk.PhotoImage(file=self.image_thought)
        else:
            caption_img = tk.PhotoImage(file=self.image_speech)
        # print(caption_img)
        self.caption_id = self.create_image(0, 0, anchor=tk.NW, image=caption_img, tags=('captionimg'))

    def set_text(self, caption_text=None):
        if not caption_text and not self.caption_text:
            self.set_text('')
        self.caption_text = caption_text

    def get_text(self):
        if not self.caption_text:
            return ''
        return self.caption_text


if __name__ == "__main__":
    root = tk.Tk()
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    caption = CanvasCaption(root)
    caption.create_caption("Ahoy!")

    root.mainloop()
