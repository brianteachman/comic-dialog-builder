from tkinter import *
from tkinter import ttk
#
_caption_id = 0


class Caption:
    """ """
    def __init__(self, canvas, caption_text=None):
        self.setId()
        self.canvas = canvas
        if caption_text:
            self.setCaptionText(caption_text)

    def createCaption(self, caption_text=None):
        if not caption_text:
            caption_text = self.text
        # bubble = PhotoImage(file='spb-300x165.png')
        self.canvas.create_image(0, 0, anchor=NW, image=bubble)
        self.canvas.create_text(75, 25, anchor=NW, text=caption_text, width=200)

    def setId(self):
        global _caption_id
        _caption_id += 1
        self.id = _caption_id

    def getId(self):
        return self.id

    def setCaptionText(self, caption_text):
        self.text = caption_text

    def getCaptionText(self):
        return self.text

    def setPosX(self):
        """ """

    def setPosY(self):
        """ """


if __name__ == '__main__':
    canvas = Canvas(Tk())
    for i in range(10):
        caption = Caption(canvas)
        print(i, caption.getId())
