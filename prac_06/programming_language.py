"""
Intermediate Exercises
Estimate: 30 minutes
Actual: 18 minutes
"""

class ProgrammingLanguage:

    def __init__(self, name="", type="", reflection=bool, year=0):
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.type} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.type == "Dynamic"