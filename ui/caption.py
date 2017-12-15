import tkinter as tk
from PIL import ImageTk, Image


class Caption:
    """ """
    text = ''

    lastx = None
    lasty = None
    speech_bubble = 'imgs/spb-300x165.png'
    thought_bubble = 'imgs/thought.png'

    long_sample = ("I am the hope of the universe. I am the answer to all living things "
                   "that cry out for peace. I am protector of the innocent. I am the "
                   "light in the darknes"
                   "s. I am truth. Ally to good! Nightmare to you!"
                   )

    def __init__(self, canvas, caption_text=None, bubble_type='speech', position={'x': 0, 'y': 0}):
        self.canvas = canvas
        if not caption_text:
            self.text = caption_text
        self.type = bubble_type  # 'speech' or 'thought'
        self.speech_img = ImageTk.PhotoImage(Image.open(self.speech_bubble))
        self.thought_img = ImageTk.PhotoImage(Image.open(self.thought_bubble))
        self.lastx, self.lasty = position

        if bubble_type == 'thought':
            bg_image = self.thought_img
            text_posx = position['x'] + 50
            text_posy = position['y'] + 50
        else:
            bg_image = self.speech_img
            text_posx = position['x'] + 75
            text_posy = position['y'] + 25

        self.cid = self.canvas.create_image(position['x'], position['y'], anchor=tk.NW, image=bg_image)
        caption_tag = 'caption-{}'.format(int(self.cid / 2))  # local caption id
        layer_tag = 'layer-{}'.format(1)
        self.canvas.itemconfig(self.cid, tag=(caption_tag, layer_tag))

        # caption text
        self.tid = self.canvas.create_text(text_posx, text_posy,
                                           anchor=tk.NW,
                                           width=200,
                                           text=caption_text,
                                           tags='caption-text')
        # caption_text_tag = 'caption-{}-text'.format(self.cid)
        # canvas.addtag_withtag(caption_text_tag, tid)
        self.canvas.itemconfig(self.tid, tag=(caption_tag, layer_tag))

        print(caption_tag)

