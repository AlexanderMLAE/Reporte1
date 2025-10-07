import csv

# alr how we gon do this
# nested dicts?
# one dictionary with each course as a key and another dictionary as a value
# all data per specific course will be on the nested dict
# sounds good?


def readFile(): 

    counter = 0

    with open('cursos.csv', newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            print(row)
            counter += 1
    return counter

# Find total amount

def findTotal():

    total = readFile()

    print("Total of courses: ", total)

findTotal()


