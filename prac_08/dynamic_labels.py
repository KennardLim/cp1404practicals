from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    """Main program - Kivy app to dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, *args):
        """Construct main app."""
        super().__init__(*args)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Jack Black", "Ziggy Zag"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)

DynamicLabelsApp().run()