from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_PER_MILE = 1.60934
DEFAULT_VALUE = 0

class ConvertMilesToKilometresApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometres"""
    result = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.result = "54.717"
        return self.root

    def handle_calculate(self):
        """Handle calculation (could be button press or other call), output result to label widget"""
        # self.root.ids.output_label.text = self.get_valid_input() * KM_PER_MILE
        self.result = str(self.get_valid_input() * KM_PER_MILE)

    def handle_increment(self, change):
        """Handle up/down button, updates the text input with the changed value
        change: the amount the text input is changed"""
        self.root.ids.input_number.text = str(self.get_valid_input() + change)

    def get_valid_input(self):
        """get a valid input from the text input and return it as a float,
        if it isn't a float, return 0"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return DEFAULT_VALUE

ConvertMilesToKilometresApp().run()