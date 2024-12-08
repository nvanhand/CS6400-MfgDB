from widgets import *
from kivyImports import *

class SpinnerSelect(LabelledBox):
    options = ListProperty([])
    def __init__(self,  **kwargs):
        super(SpinnerSelect, self).__init__(**kwargs)

    def on_spinner_select(self, text):
        self.ids.input_id.text = text

    def get(self):
        return self.label_text, self.ids.input_id.text

class MultiSelectSpinner(Button):
    # Adapted from https://stackoverflow.com/a/36655886
    dropdown = ObjectProperty(None)
    values = ListProperty([])
    selected_values = ListProperty([])
    def __init__(self, **kwargs):
        self.bind(dropdown=self.update_dropdown)
        self.bind(values=self.update_dropdown)
        super(MultiSelectSpinner, self).__init__(**kwargs)
        self.bind(on_release=self.toggle_dropdown)
    def set_values(self, values):
        self.values = values

    def toggle_dropdown(self, *args):
        if self.dropdown.parent:
            self.dropdown.dismiss()
        else:
            self.dropdown.open(self)

    def update_dropdown(self, *args):
        if not self.dropdown:
            self.dropdown = DropDown()
        values = self.values
        if values:
            if self.dropdown.children:
                self.dropdown.clear_widgets()
            for value in values:
                b = Factory.MultiSelectOption(text=value)
                b.bind(state=self.select_value)
                self.dropdown.add_widget(b)

    def select_value(self, instance, value):
        if value == 'down':
            if instance.text not in self.selected_values:
                self.selected_values.append(instance.text)
        else:
            if instance.text in self.selected_values:
                self.selected_values.remove(instance.text)

    def on_selected_values(self, instance, value):
        if value:
            self.text = ', '.join(value)
        else:
            self.text = ''

class MultiSpinner(LabelledBox):
    options = ListProperty(['test1', 'test2'])
    label_text = StringProperty('')
    def __init__(self, **kwargs):
        super(MultiSpinner, self).__init__(**kwargs)

    def get(self):
        return self.label_text, self.ids.mss.text

