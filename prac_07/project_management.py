"""
Project Management Program
Estimate: 2 hour 30 minutes
Actual: 5 hour 30 minutes
"""

from project import Project
from operator import attrgetter
import datetime
import os

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"  
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n" 
        "- (U)pdate project\n"
        "- (Q)uit")
DATA_FILENAME = "projects.txt"

def main():
    """Run a project manager where the user can save and load projects from a file,
        display projects in various ways, add new projects, and update their projects"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects_from_file(DATA_FILENAME)
    print(f"Loaded {len(projects)} projects from projects.txt")
    print(MENU)
    choice = input(">>> ").capitalize()
    while choice != "Q":
        if choice == "L":
            filename = get_valid_filename("Filename to load projects from: ")
            projects = load_projects_from_file(filename)
        elif choice == "S":
            filename = get_valid_filename("Filename to save projects to: ")
            save_project_to_file(filename, projects)
        elif choice == "D":
            display_projects_by_completion(projects)
        elif choice == "F":
            filter_date_string = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
            display_projects_after_date(projects, filter_date)
        elif choice == "A":
            projects.append(get_new_project())
        elif choice == "U":
            display_projects_with_index(projects)
            project_number = int(input("Project choice: "))
            completion_percentage = get_valid_percent("New Percentage: ")
            priority = int(input("New Priority: "))
            update_project(projects, project_number, completion_percentage, priority)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").capitalize()
    choice = input(f"Would you like to save to {DATA_FILENAME}? ").lower()
    if choice == "y" or "yes":
        save_project_to_file(DATA_FILENAME, projects)
    print("Thank you for using custom-built project management software.")

def load_projects_from_file(filename):
    """Read the specified text file and process each line into a project class object
        to put into the projects list"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            project_data = line.strip("\n").split("\t")
            project = Project(project_data[0], datetime.datetime.strptime(project_data[1], "%d/%m/%Y").date(),
                      int(project_data[2]), float(project_data[3]), int(project_data[4]))
            projects.append(project)
    return projects

def save_project_to_file(filename, projects):
    """Writes the projects into the specified text file with each line written containing
        the projects class"""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects_by_completion(projects):
    """Displays the projects into complete and incomplete projects"""
    print("Incomplete projects: ")
    for project in sorted([project for project in projects if not project.is_complete()]):
        print(f"\t{project}")
    print("Completed projects: ")
    for project in sorted([project for project in projects if project.is_complete()]):
        print(f"\t{project}")

def display_projects_after_date(projects, filter_date):
    """Display the projects that were created before the given date,
        and then later sorted by date"""
    for project in sorted([project for project in projects if project.start_date > filter_date],
                          key=attrgetter("start_date")):
        print(project)

def display_projects_with_index(projects):
    """Display the projects along with their index number"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

def get_new_project():
    """Get valid attributes and returns a new project from the given attributes"""
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ")
    cost_estimate = get_valid_float("Cost estimate: $")
    completion_percentage = get_valid_percent("Percent complete: ")
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    return project

def update_project(projects, project_index, new_completion_percentage, new_priority):
    """Update a project to change its percentage and or priority,
        if the new value is blank then the value won't be changed"""
    if new_completion_percentage != "":
        projects[project_index].completion_percentage = new_completion_percentage
    if new_priority != "":
        projects[project_index].priority = new_priority

def get_valid_filename(prompt):
    """Get a valid input that is a file that exists"""
    while True: # used while True loop to infinitely loop until the input is valid
        user_input = input(prompt)
        if os.path.exists(user_input) and os.path.isfile(user_input) and user_input.endswith(".txt"):
            return user_input
        else:
            print("Number must be >= 0.")

def get_valid_number(prompt):
    """Get a valid input that is a non-negative integer"""
    while True: # used while True loop to infinitely loop until the input is valid
        try:
            user_input = int(input(prompt))
            if user_input >= 0:
                return user_input
            else:
                print("Number must be >= 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")

def get_valid_float(prompt):
    """Get a valid input that is a non-negative float"""
    while True: # used while True loop to infinitely loop until the input is valid
        try:
            user_input = float(input(prompt))
            if user_input >= 0:
                return user_input
            else:
                print("Decimal must be >= 0.")
        except ValueError:
            print("Invalid input; enter a valid decimal.")

def get_valid_percent(prompt):
    """Get a valid input that is a non-negative percentile number"""
    while True: # used while True loop to infinitely loop until the input is valid
        try:
            user_input = int(input(prompt))
            if 0 <= user_input <= 100:
                return user_input
            else:
                print("Percent must be between 0 and 100 (inclusive).")
        except ValueError:
            print("Invalid input; enter a valid percent.")

def get_valid_date(prompt):
    """Get a valid input that is a date in dd/mm/yyyy format"""
    while True: # used while True loop to infinitely loop until the input is valid
        try:
            user_input = datetime.datetime.strptime(input(prompt), "%d/%m/%Y").date()
            return user_input
        except:
            print("Invalid input; enter a valid date.")

main()

"""
Name	Start Date  Priority    Cost Estimate	Completion Percentage
Build Car Park	12/09/2021	2	600000.0	95
Mow Lawn	31/10/2022	3	3.0	0
Organise Pantry	20/07/2022	1	25.0	55
Record Music Video	01/12/2022	9	250000.0	0
Read 7 Habits Book	13/12/2021	6	99.0	100
"""