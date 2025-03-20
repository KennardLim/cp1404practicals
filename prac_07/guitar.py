"""
Guitars!
Estimate: 50 minutes
Actual: 55 minutes
"""

from datetime import date

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Construct a ProgrammingLanguage from the given values.

        name: string, the guitar's model name
        year: integer, the year the guitar was created
        cost: float, the cost of the guitar in USD($)
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        return f"name={self.name}, year={self.year}, cost={self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return date.today().year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
