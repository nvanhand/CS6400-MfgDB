
from BuildScreen import *
from kivyImports import *
from widgets import *
from datetime import datetime as dt

homedir = os.path.join(os.getcwd(), '3_gui')
os.chdir(homedir)
assetdir = os.path.join(homedir, 'assets')
localStorage = os.path.join(homedir, 'imageStore')

screenfile =  'widgets/BuildScreen.kv'
Builder.load_file('widgets/widgets.kv')
Builder.load_file(screenfile)
class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session = {}
    def get_screens(self):
        with open('widgets/BuildScreen.kv', 'r') as f:
            kv_string = f.read()
        kv_string = kv_string.replace('@', '>')
        return re.findall(r'<(.*?)>', kv_string)
    def build(self):
        screen_names = self.get_screens()
        Window.bind(on_request_close=self.on_request_close)
        self.assetdir = assetdir
        self.screenManager = ScreenManager()
        self.initJSON()
        for screen in screen_names:
            screenname = getattr(sys.modules['BuildScreen'], screen)
            self.screenManager.add_widget(screenname(screen))

        return self.screenManager

    def initJSON(self):
        self.session_start = dt.now().strftime("%Y-%m-%d_%H-%M")
        self.session_name = f'.session/.session_{self.session_start}.json'
        with open(self.session_name, 'w') as json_file:
            json.dump({}, json_file)

    def on_request_close(self, *args):
        # https://stackoverflow.com/questions/54501099
        popup = WindowPopup(title='Exit', text='Are you sure you want to quit? \n Your progress may not be saved.  \n Click outside of the popup to continue.')
        popup.ids.btn.bind(on_release=self.shutdown)
        popup.open()
        return True

    def shutdown(self, inst):
        try:
            with open(self.session_name, 'r') as file:
                data = json.load(file)
                if data == {} :
                    os.remove(self.session_name)
        except FileNotFoundError:
            print('File Not Found. Your session will not be saved.')
        self.stop()


if __name__ == '__main__':
    MyApp().run()

