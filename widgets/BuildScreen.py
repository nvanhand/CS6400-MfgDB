from PIL import Image
from widgets import *
from spinners import *

class StartScreen(MyScreen):
    pass
class Maintenance(MyScreen):
    pass
class BuildScreen(MyScreen):
    def camera_settings(self):
        self.cam1_on = self.ids.cam1 == 'down'
        self.cam2_on = self.ids.cam2 == 'down'

class PostBuild(MyScreen):
    pass

class CamScreen(MyScreen):
    image_source = StringProperty('')
    image_x = NumericProperty(2048)
    image_y = NumericProperty(1824)

class ClickCam(MyScreen):
    image_source = StringProperty('')
    cam1 = BooleanProperty(False)
    cam2 = BooleanProperty(False)
    def inital_clickcamera(self):
        pass