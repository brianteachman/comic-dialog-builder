from tkinter import *
from tkinter import ttk
#
_caption_id = 0


class Caption:
    """ """
    caption_text = ''

    def __init__(self, canvas, caption_text=None):
        self.setId()
        self.canvas = canvas
        if caption_text:
            self.setText(caption_text)

    # def __del__(self):
    #     global _caption_id
    #     _caption_id = 0

    def setId(self):
        global _caption_id
        _caption_id += 1
        self.id = _caption_id

    def overrideId(self, caption_id):
        global _caption_id
        _caption_id = caption_id
        self.id = caption_id

    def getId(self):
        return self.id

    def createCaption(self, caption_text=None):
        self.setText(caption_text)

        bubbleimg = PhotoImage(file='imgs/spb-300x165.png')
        self.canvas.create_image(0, 0, anchor=NW, image=bubbleimg, tags=('bubbleimg'))
        self.canvas.create_text(75, 25, anchor=NW, text=caption_text, width=200)

    def setText(self, caption_text=None):
        if not caption_text and not self.caption_text:
            self.setText('')
        self.caption_text = caption_text

    def getText(self):
        if not self.caption_text:
            return ''
        return self.caption_text

    def setPosX(self):
        """ """

    def setPosY(self):
        """ """


if __name__ == '__main__':
    canvas = Canvas(Tk())
    for i in range(10):
        caption = Caption(canvas)
        caption.createCaption("Something_"+str(caption.getId()))
        print(i, caption.getId(), caption.getText())

    caption = Caption(canvas)
    caption.createCaption('Aha!')
    print( caption.getId(), caption.getText() )
