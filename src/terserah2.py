# tucil3 :))

def readFile(namaFile):
    arrFile = []
    openFile = open(namaFile, 'r')
    readFile = openFile.readlines()
    for line in readFile:
        each = line.rstrip('\n')
        arrFile.append(each)
    return arrFile

def euclideanDistance(titika, titikb):
    # titika = arrVertex[i]
    # titikb = arrVertex[j]
    return (((arrVertexCoordinate[titika][0]-arrVertexCoordinate[titikb][0])**2)+((arrVertexCoordinate[titika][1]-arrVertexCoordinate[titikb][1])**2))**0.5

def vertexCoordinate(arrFile):
    arrVertexCor = []
    i = 1
    while (i < int(arrFile[0])+1):
        arrVertexCor.append(arrFile[i].split())
        i += 1

    # misahin vertex
    arrVertex = []
    for i in range(len(arrVertexCor)):
        arrVertex.append(arrVertexCor[i][0])
    
    # misahin coordinate
    arrCoordinate = []
    for i in range(len(arrVertexCor)):
        coordinate = []
        for j in range(len(arrVertexCor[i])):
            if (j != 0):
                coordinate.append(arrVertexCor[i][j])
        arrCoordinate.append(coordinate)
    for i in range(len(arrCoordinate)):
        for j in range(2):
            arrCoordinate[i][j] = int(arrCoordinate[i][j])
    vertexCoordinate = dict(zip(arrVertex,arrCoordinate))
    return vertexCoordinate

def makeListVertex(arrFile):
    arrVertexCor = []
    i = 1
    while (i < int(arrFile[0])+1):
        arrVertexCor.append(arrFile[i].split())
        i += 1
    arrVertex = []
    for i in range(len(arrVertexCor)):
        arrVertex.append(arrVertexCor[i][0])
    return arrVertex

def makeMatrix(arrFile):
    i = int(arrFile[0])+1
    arrMatrix = []
    while (i < int(arrFile[0])*2+1):
        arrMatrix.append(arrFile[i].split())
        i += 1
    return arrMatrix

def makeGraph(arrMatrix, arrVertex):
    arrTetangga = []
    for i in range(len(arrMatrix)):
        vertex = []
        for j in range(len(arrMatrix[i])):
            if (arrMatrix[i][j] == '1'):
                vertex.append(arrVertex[j])
        arrTetangga.append(vertex)
    dictGraph = dict(zip(arrVertex,arrTetangga))
    return dictGraph

def makeGraphCost(arrMatrix, arrVertex, arrVertexCoordinate):
    arrTetangga = []
    for i in range(len(arrMatrix)):
        vertex = []
        for j in range(len(arrMatrix[i])):
            if (arrMatrix[i][j] == '1'):
                cost = euclideanDistance(arrVertex[i],arrVertex[j])
                vertex.append(cost)
        arrTetangga.append(vertex)
    dictGraphCost = dict(zip(arrVertex,arrTetangga))
    return dictGraphCost

def heu(arrVertex, tujuan):
    nilaih = []
    for i in range(len(arrVertex)):
        nilaih.append(euclideanDistance(arrVertex[i], tujuan))
    dictH = dict(zip(arrVertex, nilaih))
    return dictH
        


# main program
if __name__ == '__main__':
    
    namaFile = "../test/tes.txt"
    arrFile = readFile(namaFile)

    #prep
    arrVertexCoordinate = vertexCoordinate(arrFile)
    arrVertex = makeListVertex(arrFile)
    listtempat = set(arrVertex)
    arrMatrix = makeMatrix(arrFile)
    dictGraph = makeGraph(arrMatrix, arrVertex)
    dictGraphCost = makeGraphCost(arrMatrix, arrVertex, arrVertexCoordinate)

    # print("arrVertexCoordinate: ",arrVertexCoordinate)
    # print("arrvertex:", arrVertex)
    # print("dictgraph:", dictGraph)
    # print("ngetes cek koord:", arrVertexCoordinate["A"][0])
    # print("dictGraphCost: ", dictGraphCost)

    asal = input("Masukkan lokasi asal: ")
    while asal not in listtempat:
        print("Tempat tidak tersedia. Masukkan tempat yang sesuai.")
        asal = input("Masukkan lokasi asal: ")

    tujuan = input("Masukkan lokasi tujuan: ")
    while tujuan not in listtempat:
        print("Tempat tidak tersedia. Masukkan tempat yang sesuai.")
        tujuan = input("Masukkan lokasi tujuan: ")
    
    dictH = heu(arrVertex, tujuan)
    # print(dictH)