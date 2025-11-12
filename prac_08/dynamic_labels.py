"""
Dynamic Labels Exercise
Simple Names List App
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Simple Kivy app for dynamic labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Joker", "Skull", "Panther", "Fox", "Queen", "Noir", "Crow", "Violet"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
