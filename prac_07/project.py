"""
Project Management Program
Estimate: 2 hour 30 minutes
Actual: 5 hour 30 minutes
"""

from datetime import date

class Project:

    def __init__(self, name="", start_date=date.today(), priority=0,
                 cost_estimate=0.0, completion_percentage=0):
        """Construct a Project object from the given values:

        name: string, the project's name
        start_date: datetime, the date at which the project started
        priority: integer, the priority value of the project, the higher it is the more important the project
        cost_estimate: float, an estimate of how much it would cost to do the project (USD)
        completion_percentage: integer, a percentage indicating the project's progress to completion
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a machine-readable representation of a project"""
        return (f"{self}, name={self.name}, start_date={self.start_date}, priority={self.priority}, "
                f"cost_estimate={self.cost_estimate}, completion_percentage={self.completion_percentage}")

    def __str__(self):
        """Return the string representation of a project"""
        return (f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def __eq__(self, other):
        """Defines behavior for the == operator between projects using their priority"""
        return self.priority == other.priority

    def __ne__(self, other):
        """Defines behavior for the != operator between projects using their priority"""
        return self.priority != other.priority

    def __lt__(self, other):
        """Defines behavior for the < operator between projects using their priority"""
        return self.priority < other.priority

    def __gt__(self, other):
        """Defines behavior for the > operator between projects using their priority"""
        return self.priority > other.priority

    def __le__(self, other):
        """Defines behavior for the <= operator between projects using their priority"""
        return self.priority <= other.priority

    def __ge__(self, other):
        """Defines behavior for the >= operator between projects using their priority"""
        return self.priority >= other.priority

    def is_complete(self):
        """Returns a bool of whether a project is complete or not based on its completion percentage"""
        return self.completion_percentage == 100

# Debugging code:
# project_1 = Project("Birthday Time!", date(2006, 7, 13), 5, 260.5, 35)
# project_2 = Project("Homework", date(2023, 5, 10), 2, 260.5, 30)
# project_3 = Project("Death.", date(2014, 4, 14), 4, 444.44, 44)
# print(project_1)
# print(project_2)
# print(project_3)
# print("")
# projects = [project_1, project_2, project_3]
# projects.sort(reverse=True)
# for project in projects:
#     print(project)

