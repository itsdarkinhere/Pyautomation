import csv
import webbrowser

filename = "courses.csv"

class Course:
    def __init__(self, name, link):
        self.name = name
        self.link = link

def main():
    fields = []
    rows = []
    classes = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)

    for row in rows:
        classes.append(Course(row[0], row[1]))

    print(fields[0].ljust(45, ' '), "Number".rjust(5, ' '), '\n')

    for course in classes:
        print(course.name.ljust(45, ' '), str((classes.index(course) + 1)).rjust(5, ' '))

    chosenClass = int(input("\nWhich course number do you want to join?\n"))

    webbrowser.open(classes[chosenClass-1].link)

if __name__ == '__main__':
    main()