"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to display subject data."""
    subject_records = load_subject_records(FILENAME)
    print_subject_details(subject_records)


def load_subject_records(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_records = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_record = parts
        subject_records.append(subject_record)
    input_file.close()
    return subject_records


def print_subject_details(subject_records):
    """Print subject details including subject, lecturer and number of students with formatting."""
    for subject_record in subject_records:
        print(f"{subject_record[0]} is taught by {subject_record[1]:12} and has {subject_record[2]:3} students")


main()
