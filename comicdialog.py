"""

Version: 0.0.1

Links:
----------------------------------------------------------------
1. https://docs.python.org/3/library/tkinter.html
2. http://www.tkdocs.com/widgets/index.html
3. http://www.tkdocs.com/tutorial/widgets.html
4. https://pillow.readthedocs.io/en/4.2.x/
5. https://pillow.readthedocs.io/en/4.2.x/reference/index.html
6. http://effbot.org/tkinterbook/tkinter-index.htm
7. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
8. https://wiki.python.org/moin/TkInter

"""
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageFont, ImageDraw
import logging


class ComicDialogBuilder(ttk.Frame):
    """
    Comic Strip Builder for my son, Logan. <3
    """

    def __init__(self, parent):
        """ Prepare the frame and call the GUI initialization method. """

        ttk.Frame.__init__(self, parent)
        self.parent = parent

        # Bindings
        self.parent.bind('<1>', self.leftClick)

        # Setup main container
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.status = StringVar()
        self.status.set('stop')

        # Load UI
        self.loadMenuBar()
        self.exampleScene()
        self.loadEditor()

        # ttk.Sizegrip(self.parent).grid(column=999, row=999, sticky=(S, E))

    # -------------------------------------------------------------------------

    def exampleScene(self, dialog=''):
        """ Layer PIL.Image objects to compose a scene """
        self.setSceneTitle('Vageta wont be fooled again')

        # sceneBackground = self.setBackground(''imgs/pico-geta-500x241.gif'', (500, 241))
        self.scene = self.setSceneBGImage('imgs/goku-vs-vegeta-1920-1080.jpg', (800, 449))

        # Add speech bubble over Goku's head
        self.setDialog(self.scene, 'Your shoelace is untied.', bbox=(150, 120), resizebbox=(300, 80))
        # self.setDialog(self.scene, 'Your shoelace is untied.', bbox=(150, 120))

        # Add thought bubble over Vegeta's head and speech bubble under his mouth
        self.setDialog(self.scene, 'Yeah right!',
                       bbox=(290, 280), resizebbox=(200, 90), transpose='rotate-180')
        self.setDialog(self.scene, 'Not falling for that again!', type='thought',
                       bbox=(570, 20), resizebbox=(200, 90))

        self.sceneImage = self.scene

        # Convert the PIL.Image object into a TkPhoto object
        self.scene = ImageTk.PhotoImage(self.scene)

        self.loadScene(self.scene)

        print(self.sceneTitle + ', take 1.')

    # -------------------------------------------------------------------------

    def loadMenuBar(self):
        """ Add title bar to Window """
        self.titleBar = ttk.Label(self.parent, text='Menu stuff here...')
        # it's important to add this before creating menu
        self.parent.option_add('*tearOff', FALSE)
        # Without it, each of your menus (on Windows and X11) will start with
        # what looks like a dashed line, and allows you to "tear off" the menu
        # so it appears in its own window.

        menubar = Menu(self.parent)  # This method doesn't create two windows.
        self.parent.config(menu=menubar)

        # -----------------------------------------------------------------------------
        # Top-level menu items
        # -----------------------------------------------------------------------------

        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menu_help = Menu(menubar, name='help')
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Edit')
        menubar.add_cascade(menu=menu_help, label='Help')

        menu_help.add_separator()

        # -----------------------------------------------------------------------------
        # File menu items
        # -----------------------------------------------------------------------------

        # menu_file.add_command(label='New', command=newFile)
        # menu_file.add_command(label='Open...', command=openFile)
        menu_file.add_command(label='Save', command=self.saveScene)
        # menu_file.add_command(label='Close', command=closeFile)

        # menu_file.add_separator()  # ---------------------------------------------------

        menu_file.add_command(label='Quit', command=self.parent.quit)

        # -----------------------------------------------------------------------------
        # Edit menu items
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------------------------
        # Help menu items
        # -----------------------------------------------------------------------------

        menu_help.add_command(label='About ComicDialog')

    def setSceneBGImage(self, backdrop_file, resize=None):
        """ Returns correctly sized background image """
        scene = Image.open(backdrop_file) # PIL.Image object
        if resize:
            scene = scene.resize(resize)
        # query image info
        # print( scene.info.get('icc_profile') )
        # print( scene.info.get('exif') )
        return scene

    def loadScene(self, scene_image):
        """ Adds composite scene (PIL.ImageTk) to Window """
        self.backgroundImage = ttk.Label(self.parent, image=scene_image)
        self.backgroundImage.grid(row=1, column=0, sticky=(N, S, E, W))

    def loadSceneCanvas(self, scene_image):
        """ Adds composite scene (PIL.ImageTk) to Window """
        canvas = Canvas(self.parent)
        self.backgroundImage = ttk.Frame(self.parent)
        self.backgroundImage.grid(row=1, column=0, sticky=(N, S, E, W))

    def loadEditor(self):
        """ Image Dialog Editor """
        editor = ttk.Labelframe(self.parent, text='Scene Editor', padding="3 3 12 12")
        # editor = ttk.Frame(self.parent, padding="3 3 12 12")
        editor.grid(row=2, column=0, sticky=(N, W, E, S))

        dialog = StringVar()
        ttk.Entry(editor, textvariable=dialog, width=25).grid(row=0, column=0, sticky=(W, E))
        ttk.Separator(self.parent, orient=HORIZONTAL)

        ttk.Button(editor, text="Update", command=self.updateScene).grid(row=1, column=0, sticky=E)
        ttk.Label(editor, textvariable=self.status).grid(row=1, column=1, sticky=(W, E))
        ttk.Separator(self.parent, orient=HORIZONTAL)

        ttk.Button(self.parent, text="Close", command=self.parent.quit).grid(row=2, column=0, sticky=E)

    def updateScene(self):
        """ Update Frame upon event """
        self.status.set('Updating')
        print('Scene ' + self.status.get()+'.')
        self.saveScene(self.sceneImage)
        self.status.set('Saved')

    def setDialog(self, scene, dialog, bbox, type='speech', resizebbox=None, transpose=None):
        """ Place (layer) a dialog box over a scene """
        if type == 'speech':
            sandbox = Image.open('imgs/spb-300x165.png') # PIL.Image
        else: #if type == 'thought':
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
        self.setActorCaption(sandbox, dialog, (w-(w-65), h-(h-30)))
        scene.paste(sandbox, bbox, sandbox)

    def setActorCaption(self, image, dialog='Hello', bbox=(0, 0), text_color='black'):
        """ Convert text to an image for layering

            Links:
            1. https://pillow.readthedocs.io/en/4.2.x/reference/ImageFont.html
            2. https://pillow.readthedocs.io/en/4.2.x/reference/ImageDraw.html
        """
        font = ImageFont.truetype("fonts/FreeMono.ttf", 15)
        draw = ImageDraw.Draw(image) # PIL.ImageDraw.Draw( PIL.Image )
        # draw.multiline_text(bbox, dialog, font=font, fill=text_color)
        # PIL.ImageDraw.Draw.multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left")
        draw.multiline_text(bbox, dialog, font=font, fill=(0, 0, 0, 192))

    def run(self):
        self.parent.mainloop()

    def leftClick(self, event):
        """ """
        mouse_x, mouse_y = event.x, event.y
        print('{}, {}'.format(mouse_x, mouse_y))

    # Utilities ---------------------------------------------------------------

    def setSceneTitle(self, title):
        """ Set Scene title and file slug """
        self.sceneTitle = title
        title = title.replace(' ', '-')
        self.sceneFileSlug = title.lower()

    def saveScene(self, scene=None):
        """ Write scene to file

            Links:
            1. https://pillow.readthedocs.io/en/4.2.x/reference/Image.html#PIL.Image.Image.save
            2. https://pillow.readthedocs.io/en/4.2.x/handbook/image-file-formats.html
        """
        if not scene:
            scene = self.sceneImage
        scene.save('imgs/saves/'+self.sceneFileSlug+'.png', 'png', icc_profile=scene.info.get('icc_profile'))
        scene.save('imgs/saves/'+self.sceneFileSlug+'.jpg', 'jpeg', icc_profile=scene.info.get('icc_profile'))

    # -------------------------------------------------------------------------
