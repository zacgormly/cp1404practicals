"""
Project Management Program
Estimated Time: 70 minutes
Actual Time: ??
"""

from operator import attrgetter
from datetime import datetime
from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
FAREWELL_MESSAGE = "Thank you for using custom-built project management software."
DEFAULT_FILE = "projects.txt"


def main():
    """Program for Project Management: Load, Save, Display, Filter, Add, Update Projects."""
    print(WELCOME_MESSAGE)
    projects = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            incomplete_projects = sort_projects(determine_incomplete_projects(projects))
            complete_projects = sort_projects(determine_complete_projects(projects))
            display_projects("Incomplete projects:", incomplete_projects)
            display_projects("Completed projects:", complete_projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    confirmation = input("Would you like to save to projects.txt? ").upper()
    if is_default_save(confirmation):
        save_projects(projects, DEFAULT_FILE)
        print(f"Saved {len(projects)} projects to {DEFAULT_FILE}")
    print(FAREWELL_MESSAGE)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    chosen_project_index = int(input("Project choice: "))
    print(projects[chosen_project_index])
    new_completion_percentage = input("New Percentage: ")
    if new_completion_percentage != "":
        projects[chosen_project_index].completion_percentage = int(new_completion_percentage)
    new_priority = input("New Priority: ")
    if new_priority != "":
        projects[chosen_project_index].priority = int(new_priority)


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion_percentage))


def filter_projects(projects):
    """Filter projects based on inputted date."""
    inputted_date_string = input("Show projects that start after date (dd/mm/yy): ")
    inputted_date = datetime.strptime(inputted_date_string, "%d/%m/%Y").date()
    projects.sort(key=Project.determine_date)
    for project in projects:
        if project.determine_date() >= inputted_date:
            print(project)


def display_projects(title, projects):
    """Display a title and formatted list of projects."""
    print(title)
    for project in projects:
        print(f"  {project}")


def determine_incomplete_projects(projects):
    """Determine which projects are incomplete."""
    return [project for project in projects if project.completion_percentage != 100]


def determine_complete_projects(projects):
    """Determine which projects are complete."""
    return [project for project in projects if project.completion_percentage == 100]


def sort_projects(projects):
    """Sort projects based on priority."""
    return sorted(projects, key=attrgetter("priority"))


def save_projects(projects, filename):
    """Save projects to file with correct data protocol."""
    with open(filename, "r") as in_file:
        header = in_file.readline()  # Store header to add later
    with open(filename, "w") as out_file:
        project_lines = [f"{project.name}\t{project.start_date}\t{project.priority}"
                         f"\t{project.cost}\t{project.completion_percentage}" for project in projects]
        joined_project_lines = "\n".join(project_lines)  # Avoid trailing newline
        out_file.write(header + joined_project_lines)


def is_default_save(confirmation):
    """Check if user confirms to saving data to default data file."""
    return confirmation == "Y"


def load_projects(filename):
    """Load projects from file and store in list."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Skip data header
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


if __name__ == "__main__":
    main()
