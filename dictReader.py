import csv

dictArray = []

def readFile(): 

    with open('cursos.csv', newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:
            dictArray.append(row)
    return 

# Find total amount

def findTotal():

    total = len(dictArray)
    print("Total of courses: ", total)

def findCreditsAverage():
    for curso in dictArray:
        print(curso.items())
        print(curso.get("creditos"))
readFile()

findTotal()

findCreditsAverage()

