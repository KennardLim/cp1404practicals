"""
Project Management Program
Estimate: 2 hour 30 minutes
Actual:
"""
from project import Project
from operator import attrgetter
import datetime

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"  
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n" 
        "- (U)pdate project\n"
        "- (Q)uit")

def main():
    """"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects_from_file("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")
    print(MENU)
    choice = input(">>> ").capitalize()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects_from_file(filename)
        elif choice == "S":
            filename = input("Filename to save projects to: ")
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
            display_projects_with_index()
            project_number = int(input("Project choice: "))
            completion_percentage = int(input("New Percentage: "))
            priority = int(input("New Priority: "))
            update_project(projects, project_number, completion_percentage, priority)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").capitalize()

def load_projects_from_file(filename):
    """"""
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
    """"""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects_by_completion(projects):
    """"""
    print("Incomplete projects: ")
    for project in sorted([project for project in projects if not project.is_complete()]):
        print(f"\t{project}")
    print("Completed projects: ")
    for project in sorted([project for project in projects if project.is_complete()]):
        print(f"\t{project}")

def display_projects_after_date(projects, filter_date):
    """"""
    for project in sorted([project for project in projects if project.start_date > filter_date],
                          key=attrgetter("start_date")):
        print(project)

def display_projects_with_index(projects):
    """"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

def get_new_project():
    """"""
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%dd/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    return project

def update_project(projects, project_index, new_completion_percentage, new_priority):
    """"""
    if new_completion_percentage != "":
        projects[project_index].completion_percentage = new_completion_percentage
    if new_priority != "":
        projects[project_index].priority = new_priority

main()

"""
Name	Start Date  Priority    Cost Estimate	Completion Percentage
Build Car Park	12/09/2021	2	600000.0	95
Mow Lawn	31/10/2022	3	3.0	0
Organise Pantry	20/07/2022	1	25.0	55
Record Music Video	01/12/2022	9	250000.0	0
Read 7 Habits Book	13/12/2021	6	99.0	100
"""