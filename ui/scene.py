import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import ImageTk, Image, ImageGrab
from ui.caption import Caption
from ui.layermanager import LayerManager


class Scene(tk.Canvas):

    def __init__(self, parent, height, width):
        tk.Canvas.__init__(self, parent, width=width, height=height)
        self.parent = parent
        self.layman = LayerManager(self)
        self.scene_file_slug = 'default-scene'
        self.scene_id = None
        self.scene_img = None  # PIL.Image object
        self.scene = None  # PIL.Image.PhotoImage
        self.captions = []
        self.last_x = 0
        self.last_y = 0
        # --------------------------------------------------
        # https://stackoverflow.com/a/29016234/503781
        self._drag_data = {'x': 0, 'y': 0, 'item': None}
        # --------------------------------------------------

    def new_image(self, filename, resize=None):
        # load PIL.Image from file opened in binary mode
        image = Image.open(open(filename, "rb"))
        if resize:
            image = image.resize(resize)
        return image

    def load_scene_image(self, filename, resize):
        self.scene_img = self.new_image(filename, resize)
        self.scene = ImageTk.PhotoImage(self.scene_img)

    def load_scene(self, filename, resize=None):
        self.load_scene_image(filename, resize)
        if not self.scene_id:
            self.scene_id = self.create_image(0, 0, anchor=tk.NW, image=self.scene)
        else:
            self.itemconfig(self.scene_id, image=self.scene)
        self.layman.lower_layer(self.scene_id)  # push image below captions
        print('Scene', str(self.scene_id), 'loaded')

    def add_caption(self, caption_text='', bubble_type=None):
        position = {'x': self.last_x, 'y': self.last_y}

        caption = Caption(self, caption_text, bubble_type, position)
        # if caption.text == '':
        #     caption.text = caption.long_sample

        self.bind_mouse_click(caption.cid)
        self.captions.append(caption)

        self.last_x += 100
        self.last_y += 100
        return caption.cid

    # Bindings //////////////////////////////////////////////////////

    def bind_mouse_click(self, cid):

        # pass caption id to actual event handler, which usually only gets event
        def md_handler(event, self=self, c_id=cid):
            return self._mouse_down(event, c_id)

        # pass caption id to actual event handler
        def mm_handler(event, self=self, c_id=cid):
            return self._mouse_move(event, c_id)

        self.tag_bind(cid, "<ButtonPress-1>", md_handler)  # passes extra cid arg
        self.tag_bind(cid, "<B1-Motion>", mm_handler)      # passes extra cid arg

    def _mouse_down(self, event, c_id):
        # self.scan_mark(event.x, event.y)
        # item = self.find_withtag('caption-' + str(c_id))
        # --------------------------------------------------
        # https://stackoverflow.com/a/29016234/503781
        item = self.find_closest(event.x, event.y)[0]
        tags = self.gettags(item)
        for tag in tags:
            if tag.startswith("caption-"):
                break
        self._drag_data["item"] = tag
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        print(c_id, ':', item, tags)
        # --------------------------------------------------

    def _mouse_move(self, event, c_id):
        # self.scan_dragto(event.x, event.y, gain=1)
        # --------------------------------------------------
        # https://stackoverflow.com/a/29016234/503781
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        # --------------------------------------------------

    # ///////////////////////////////////////////////////////////////

    def save_scene(self, image=None):
        if not image:
            image = self.parent
        x = image.winfo_rootx() + image.winfo_x()
        y = image.winfo_rooty() + image.winfo_y()
        x1 = x + image.winfo_width()
        y1 = y + image.winfo_height()
        filename = filedialog.asksaveasfilename(defaultextension='.jpg')
        ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
        # ImageGrab.grab().crop((x, y, x1, y1)).save("imgs/saves/new2.png")
        messagebox.showinfo(message=str(filename)+' loaded.')
