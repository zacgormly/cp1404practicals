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
    projects, is_successful = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects, is_successful = load_projects(filename)
            if is_successful:
                print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename: ")
            is_successful = save_projects(projects, filename)
            if is_successful:
                print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
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
        is_successful = save_projects(projects, DEFAULT_FILE)
        if is_successful:
            print(f"Saved {len(projects)} projects to {DEFAULT_FILE}")
    print(FAREWELL_MESSAGE)


def display_projects(projects):
    """Display projects."""
    incomplete_projects = sort_projects(determine_incomplete_projects(projects))
    complete_projects = sort_projects(determine_complete_projects(projects))
    print_projects("Incomplete projects:", incomplete_projects)
    print_projects("Completed projects:", complete_projects)


def update_project(projects):
    """Update project completion percentage and/or priority."""
    print_projects_as_numbered_list(projects)
    chosen_project_index = int(input("Project choice: "))
    print(projects[chosen_project_index])
    new_completion_percentage = input("New Percentage: ")
    if new_completion_percentage != "":
        projects[chosen_project_index].completion_percentage = int(new_completion_percentage)
    new_priority = input("New Priority: ")
    if new_priority != "":
        projects[chosen_project_index].priority = int(new_priority)


def print_projects_as_numbered_list(projects):
    """Print projects as numbered list."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")


def add_project(projects):
    """Add new project."""
    print("Let's add a new project")
    name = get_valid_string("Name: ")
    start_date = get_valid_date("Start date: ")
    priority = get_valid_integer("Priority: ")
    cost = get_valid_float("Cost estimate: $")
    completion_percentage = get_valid_integer("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost, completion_percentage))


def get_valid_string(caption):
    """Get valid non-empty string."""
    string = input(caption)
    while string == "":
        print("Input cannot be empty.")
        string = input(caption)
    return string


def get_valid_date(caption):
    """Get valid date format."""
    is_valid_input = False
    while not is_valid_input:
        start_date_string = input(caption)
        try:
            start_date = datetime.strptime(start_date_string, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Invalid date format.")
    return start_date


def get_valid_integer(caption):
    """Get integer with exception-handling."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(caption))
            is_valid_input = True
        except ValueError:
            print("Input must be an integer.")
    return number


def get_valid_float(caption):
    """Get float with exception-handling."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = float(input(caption))
            is_valid_input = True
        except ValueError:
            print("Input must be a float.")
    return number


def filter_projects(projects):
    """Filter projects based on inputted date."""
    inputted_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    for project in sorted(projects, key=Project.determine_date):
        if project.determine_date() >= inputted_date:
            print(project)


def print_projects(title, projects):
    """Print a title and formatted list of projects."""
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
    try:
        with open(filename, "r") as in_file:
            header = in_file.readline()  # Store header to add later
        with open(filename, "w") as out_file:
            project_lines = [f"{project.name}\t{project.start_date}\t{project.priority}"
                             f"\t{project.cost}\t{project.completion_percentage}" for project in projects]
            joined_project_lines = "\n".join(project_lines)  # Avoid trailing newline
            out_file.write(header + joined_project_lines)
        return True  # Indicate successful save
    except FileNotFoundError:
        print("File not found.")
    return False  # Indicate failed save


def is_default_save(confirmation):
    """Check if user confirms to saving data to default data file."""
    return confirmation == "Y"


def load_projects(filename):
    """Load projects from file and store in list."""
    projects = []
    try:
        with open(filename, "r") as in_file:
            in_file.readline()  # Skip data header
            for line in in_file:
                parts = line.strip().split("\t")
                project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
                projects.append(project)
        return projects, True  # Indicate successful load
    except FileNotFoundError:
        print("File not found.")
    return projects, False  # Indicate failed load


if __name__ == "__main__":
    main()
