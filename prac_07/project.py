"""Project Class"""

from datetime import datetime


class Project:
    """Create class representation of project object."""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Initialise a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a formatted string of name, start date, priority, estimate cost and completion."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return a formatted string of name, start date, priority, estimate cost and completion."""
        return str(self)

    def determine_date(self):
        """Determine date object from start date string."""
        return datetime.strptime(self.start_date, "%d/%m/%Y").date()

    def is_complete(self):
        """Check if completion percentage for object is 100%."""
        return self.completion_percentage == 100
