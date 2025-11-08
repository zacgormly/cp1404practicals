"""
Project Management Program
Estimated Time: 70 minutes
Actual Time: ??
"""

from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
DEFAULT_FILE = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
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
            save_projects(projects)
            print(f"Saved {len(projects)} projects from {filename}")
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def save_projects(filename):
    with open(filename, "r") as in_file:
        header = in_file.readline()
    with open(filename, "w") as out_file:
        project_lines = [f"{project.name}\t{project.start_date}\t{project.priority}"
                         f"\t{project.cost}\t{project.completion_percentage}" for project in projects]
        joined_project_lines = "\n".join(project_lines)  # Avoid trailing newline
        out_file.write(header + joined_project_lines)


def load_projects(filename):
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
