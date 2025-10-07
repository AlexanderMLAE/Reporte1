import csv

dictArray = []
noReqArray = []

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

def listaSinRequisitos():
    for curso in dictArray:
        if curso["id_prerrequisitos"] == 0:
            noReqArray.append(curso)
    print(noReqArray)

readFile()

totalCursos = findTotal()

findCreditsAverage()

listaSinRequisitos()
