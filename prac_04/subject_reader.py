"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    print_subject_detail(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data += [parts]
        print("----------")
    input_file.close()
    return data

def print_subject_detail(data):
    """Print each subject detail in data in a sentenced format"""
    max_lecturer_length = len(max([subject_detail[1] for subject_detail in data], key=len))
    max_number_of_students_length = len(max([str(subject_detail[2]) for subject_detail in data], key=len))
    for subject_detail in data:
        print(f"{subject_detail[0]} is taught by {subject_detail[1]:{max_lecturer_length}} and has {subject_detail[2]:{max_number_of_students_length}} students")

main()