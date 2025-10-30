"""Guitar Class"""

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string of..."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        return Guitar.get_age(self) >= 50
