"""Programming Language Class"""

class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=""):
        """Initialise a language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string of name, typing, reflection and year."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        """Return a string of name, typing, reflection and year for a list collection."""
        return str(self)

    def is_dynamic(self):
        """Check if language has dynamic typing."""
        return self.typing == "Dynamic"
