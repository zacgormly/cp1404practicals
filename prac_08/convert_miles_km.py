"""Miles to Kilometres Conversion Kivy App"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


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
        result = float(miles) * 1.60934
        self.output = str(result)

    def handle_increment(self, miles, increment):
        """Handle increment with up and down buttons."""
        new_miles = float(miles) + increment
        self.input = str(new_miles)


ConvertDistanceApp().run()
