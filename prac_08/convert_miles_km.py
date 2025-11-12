"""Miles to Kilometres Conversion Kivy App"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_RATE = 1.60934

class ConvertDistanceApp(App):
    """ConvertDistanceApp is a Kivy App for converting miles to kilometres."""
    output = StringProperty()
    input = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (550, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, miles):
        """Handle calculation of miles to km."""
        try:
            result = float(miles) * CONVERSION_RATE
            self.output = str(result)
        except ValueError:
            self.output = str(0.0)

    def handle_increment(self, miles, increment):
        """Handle increment with up and down buttons."""
        try:
            new_miles = float(miles) + increment
        except ValueError:
            new_miles = 0.0 + increment
        self.input = str(new_miles)


ConvertDistanceApp().run()
