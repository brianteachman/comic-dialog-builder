from PIL import Image, ImageFont, ImageDraw


class Dialog:
    """ """
    def __init__(self):
        self.stuff = "stuff"

        # invariants
        self.label = None
        self.label.bind('<1>', self.left_click)

    def set_dialog(self, scene, dialog, bbox, type='speech', resizebbox=None, transpose=None):
        """ Place (layer) a dialog box over a scene
        """
        if type == 'speech':
            sandbox = Image.open('imgs/spb-300x165.png')  # PIL.Image
        else:  # if type == 'thought':
            sandbox = Image.open('imgs/thought.png')
        if resizebbox:
            sandbox = sandbox.resize(resizebbox)
        if transpose == 'flip-x':
            sandbox = sandbox.transpose(Image.FLIP_TOP_BOTTOM)
        elif transpose == 'flip-y':
            sandbox = sandbox.transpose(Image.FLIP_LEFT_RIGHT)
        elif transpose == 'rotate-90':
            sandbox = sandbox.transpose(Image.ROTATE_90)
        elif transpose == 'rotate-180':
            sandbox = sandbox.transpose(Image.ROTATE_180)
        elif transpose == 'rotate-270':
            sandbox = sandbox.transpose(Image.ROTATE_270)
        # print(bbox[0], bbox[1])
        w = sandbox.width
        h = sandbox.height
        self.set_actor_caption(sandbox, dialog, (w - (w - 65), h - (h - 30)))
        scene.paste(sandbox, bbox, sandbox)
        # TODO: add binding

    def set_actor_caption(self, image, dialog='Hello', bbox=(0, 0), text_color='black'):
        """ Convert text to an image for layering

            Links:
            1. https://pillow.readthedocs.io/en/4.2.x/reference/ImageFont.html
            2. https://pillow.readthedocs.io/en/4.2.x/reference/ImageDraw.html
        """
        font = ImageFont.truetype("fonts/FreeMono.ttf", 15)
        draw = ImageDraw.Draw(image)  # PIL.ImageDraw.Draw( PIL.Image )
        # draw.multiline_text(bbox, dialog, font=font, fill=text_color)
        # PIL.ImageDraw.Draw.multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left")
        draw.multiline_text(bbox, dialog, font=font, fill=(0, 0, 0, 192))

