import tkinter as tk
from PIL import ImageTk, Image


class Caption:
    """ """

    lastx = None
    lasty = None
    speech_bubble = 'imgs/spb-300x165.png'
    thought_bubble = 'imgs/thought.png'

    def __init__(self, canvas, caption_text, bubble_type='speech', position={'x': 0, 'y': 0}):
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

        self.cid = canvas.create_image(position['x'], position['y'], anchor=tk.NW, image=bg_image)
        caption_tag = 'caption-{}'.format(self.cid)
        layer_tag = 'layer-{}'.format(1)
        canvas.itemconfig(self.cid, tag=(caption_tag, layer_tag))

        # caption text
        tid = canvas.create_text(text_posx, text_posy,
                                 anchor=tk.NW,
                                 width=200,
                                 text=caption_text,
                                 tags='caption-text')
        # caption_text_tag = 'caption-{}-text'.format(self.cid)
        # canvas.addtag_withtag(caption_text_tag, tid)
        canvas.itemconfig(tid, tag=(caption_tag, layer_tag))

        print(caption_tag)
