from kivyImports import *

# Set the default font size globally
LabelBase.font_size = '12sp'  # Set the default font size here
default_path = os.getcwd() # Set root 
assetdir = os.path.join(default_path, "3_gui", "assets/")
print(assetdir)

def fmt_label(label):
    return label.title().replace(' ', '')

class MyScreen(Screen):
    name = StringProperty('')
    def __init__(self, session_name, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.session = {}
        self.session_name = session_name

    def read_screen(self):
        children = {}
        for child in self.ids.content.children:
            if hasattr(child, 'get'):
                label, value = child.get()
                children[fmt_label(label)] = fmt_label(value)
        self.session[self.name] = children

    def update_session(self):
        session = App.get_running_app().session
        children = {}
        App.get_running_app().session[self.session_name] = self.session

    def date(self):
        return str(dt.datetime.now().strftime("%d/%m/%Y %H:%M"))

    def change_screen(self, choose, dir):
        self.read_inputs()
        self.update_session()
        self.manager.current = choose
        self.manager.transition.direction = dir


class FinishScreen(MyScreen):
    def __init__(self, session_name, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.buffer = []
        self.session = {}
        self.session_name = session_name
        self.update_session()
       
    def push_build():
        pass

    def finishBuild(self):
        self.read_screen()
        self.update_session()
        print(App.get_running_app().session)
        App.get_running_app().shutdown('')


class LabelledBox(BoxLayout):
    label_text = StringProperty('')
    def __init__(self, **kwargs):
        super(LabelledBox, self).__init__(**kwargs)

class BlockText(BoxLayout):
    text = StringProperty('')
    def __init__(self, text='', **kwargs):
        super(BlockText, self).__init__(**kwargs)

class InputField(LabelledBox):
    input_filter = ObjectProperty(None)
    hint_text = StringProperty('')
    field_text = StringProperty('')
    multiline = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(InputField, self).__init__( **kwargs)
    def get(self):
        return self.label_text, self.ids.text_input.text

class FolderBtn(Button):
    assetdir = StringProperty()
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.assetdir = assetdir

class FileSelect(LabelledBox):
    assetdir = StringProperty()
    col_name = StringProperty('')
    def __init__(self, **kwargs):
        super(FileSelect, self).__init__(**kwargs)
        self.assetdir = assetdir
    def getcwd(self):
        return os.getcwd()
    def open_file_dialog(self, inst):
        self.ids.input_field.text = filechooser.choose_dir(title="File path",
                                                          path=default_path)[0]
    def get(self):
        return self.col_name, self.ids.input_field.text

class WindowPopup(Popup):
    title = StringProperty("")
    text = StringProperty("")

