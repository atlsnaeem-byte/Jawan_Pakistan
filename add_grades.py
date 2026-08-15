"""Add a Grade column to student_data.csv based on the Percentage column.

Grading scale:
    A : 80 - 100
    B : 70 - 79
    C : 60 - 69
    D : 50 - 59
    F : below 50
"""

import csv

INPUT_FILE = "student_data.csv"
OUTPUT_FILE = "student_data_with_grades.csv"


def get_grade(percentage):
    """Return the letter grade for a given percentage."""
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    with open(INPUT_FILE, "r", newline="") as infile, \
         open(OUTPUT_FILE, "w", newline="") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read header and append the new column name
        header = next(reader)
        writer.writerow(header + ["Grade"])

        percentage_index = header.index("Percentage")

        for row in reader:
            if not row:            # skip any blank lines
                continue
            percentage = float(row[percentage_index])
            writer.writerow(row + [get_grade(percentage)])

    print(f"Done. Grades written to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
