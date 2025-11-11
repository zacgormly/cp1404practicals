"""Guitar Class"""

CURRENT_YEAR = 2025
VINTAGE_THRESHOLD = 50


class Guitar:
    """Create class representation of guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string of name, year and cost."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
        # return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def __repr__(self):
        """Return a formatted string of name, year and cost."""
        return str(self)

    def __lt__(self, other):
        """Return less than comparison"""
        return self.year < other.year

    def get_age(self):
        """Get age based on current year and the year guitar was created."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if guitar is vintage based on age."""
        return Guitar.get_age(self) >= VINTAGE_THRESHOLD
