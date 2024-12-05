from spinners import *
import json

from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

class MyScreen(Screen):
    def __init__(self, name,  navbar=None, session_log='', **kwargs):
        super(initScreen, self).__init__(**kwargs)
        self.name = name
        self.layout = BoxLayout()
        self.buildNavbar(navbar)
        self.add_widget(self.layout)
        self.session = session_log
        self.data_queue = []

    def read_inputs(self):
        if self.layout is not None:
            inputs = {}
            for widget in self.layout.walk():
                if hasattr(widget, 'get') and callable(getattr(widget, 'get')):
                    key, value = widget.get()
                    inputs[key] = value
            self.data_queue.append(inputs)

    def update_session(self):
        if len(self.data_queue) > 0:
            with open(self.session, 'r') as file:
                data = json.load(file)
            data[self.name] = self.data_queue.pop(0)
            with open(self.session, 'w') as file:
                json.dump(data, file, indent=4)


    def change_screen(self, choose, dir):
        self.read_inputs()
        self.update_session()
        self.manager.current = choose
        self.manager.transition.direction = dir
