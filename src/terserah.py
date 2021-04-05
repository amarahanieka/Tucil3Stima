# tucil3 :))

def readFile(namaFile):
    arrFile = []
    openFile = open(namaFile, 'r')
    readFile = openFile.readlines()
    for line in readFile:
        each = line.rstrip('\n')
        arrFile.append(each)
    return arrFile

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
# main program
namaFile = "../test/tes.txt"
arrFile = readFile(namaFile)
arrVertexCoordinate = vertexCoordinate(arrFile)
# print(arrVertexCoordinate)
arrVertex = makeListVertex(arrFile)
# print(arrVertex)
arrMatrix = makeMatrix(arrFile)
# for i in arrMatrix:
#     print(i)
dictGraph = makeGraph(arrMatrix, arrVertex)
print(dictGraph)


