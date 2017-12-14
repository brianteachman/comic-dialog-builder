from tkinter import ttk, Canvas, N, S, E, W
from PIL import Image, ImageTk
from PIL import ImageFont, ImageDraw


class SceneModel:
    """ """
    def __init__(self, canvas, scene, bg_image):
        self.bg_image = bg_image
        self.canvas = canvas
        self.model = scene


class Scene:
    """ """

    def __init__(self, parent, filename=None, resize=None):
        self.parent = parent

        # init scene invariants
        self.scene_title = "Default Scene"
        self.scene_file_slug = None  # string
        self.scene_image = None  # PIL.Image
        self.scene = None  # PIL.ImageTk.PhotoImage

        self.bg_image = None
        self.scene = None
        self.canvas = None
        if filename:
            self.bg_image = filename
            self.write_name = "test-write"
            self.scene = self.set_scene_bgimage(filename)

    def load_scene(self, scene_image):
        """ Adds composite scene (PIL.ImageTk) to Window """
        scene = ttk.Label(self.parent, image=scene_image)
        return scene.grid(row=1, column=0, sticky=(N, S, E, W))

    def set_scene_bgimage(self, backdrop_file, resize=None):
        """ Returns correctly sized background image """
        self.bg_image = backdrop_file
        scene = Image.open(backdrop_file)  # PIL.Image object
        if resize:
            scene = scene.resize(resize)
        # query image info
        # print( scene.info.get('icc_profile') )
        # print( scene.info.get('exif') )
        self.scene = scene
        return scene

    def init_scene_canvas(self):
        """ Adds composite scene (PIL.ImageTk) to Window """
        canvas = Canvas(self.parent)  # TODO: finish this
        scene_canvas = ttk.Frame(self.parent)
        return scene_canvas.grid(row=1, column=0, sticky=(N, S, E, W))

    def save_scene(self, scene=None):
        """ Write scene to file

            Links:
            1. https://pillow.readthedocs.io/en/4.2.x/reference/Image.html#PIL.Image.Image.save
            2. https://pillow.readthedocs.io/en/4.2.x/handbook/image-file-formats.html
        """
        if not scene:
            scene = self.scene
        scene.save('../imgs/saves/' + self.write_name + '.png', 'png',
                   icc_profile=scene.info.get('icc_profile'))
        # scene.save('../imgs/saves/' + self.write_name + '.jpg', 'jpeg',
        #            icc_profile=scene.info.get('icc_profile'))

    def update_scene(self):
        """ Update Frame upon event """
        # self.parent.status.set('Updating')
        # print('Scene ' + self.status.get()+'.')
        self.save_scene(self.scene)
        # self.parent.status.set('Saved')
