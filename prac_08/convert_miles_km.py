from kivy.app import App
from kivy.lang import Builder

KM_PER_MILE = 1.60934
DEFAULT_VALUE = 0.0

class ConvertMilesToKilometresApp(App):
    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self, kilometre):
        """"""
        self.root.ids.output_label.text = str(float(kilometre) * KM_PER_MILE)

    def handle_increment(self, change):
        """"""
        self.root.ids.input_number.text = str(float(self.root.ids.input_number.text) + change)

ConvertMilesToKilometresApp().run()