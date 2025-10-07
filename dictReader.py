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
        creditos = curso.get('creditos')
        print(creditos)
readFile()

totalCursos = findTotal()

findCreditsAverage()

