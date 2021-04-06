# tucil3 :))
import collections

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
        
def fn(dictGraphCost, dictH):
    return (dictGraphCost + dictH)

# def bfs(graph, asal, tujuan):
    
#     visited, queue = set(), collections.deque([asal])
#     visited.add(asal)
#     vertex = ''
#     urutan = []

#     while queue and str(vertex) != tujuan:
#         # Dequeue a vertex from queue
#         vertex = queue.popleft()
#         # print(str(vertex) + " ", end="\n")
#         urutan.append(str(vertex))
#             # If not visited, mark it as visited, and
#             # enqueue it
#         for tetangga in graph[vertex]:
#             if tetangga not in visited:
#                 visited.add(tetangga)
#                 queue.append(tetangga)
    
#     # print('visited:', visited)
#     if tujuan not in urutan:
#         print(asal,"&",tujuan,"tidak terhubung.")
#     else:
#         for x in urutan:
#             print(x, end =' ')

# def astar1(dictGraph, asal, tujuan, dictH, arrVertex):
    
#     visited = set()
#     queue = collections.deque([asal])
#     visited.add(asal)
#     vertex = ''
#     urutan = []

#     while queue and str(vertex) != tujuan:
#         # Dequeue a vertex from queue
#         vertex = queue.popleft()
        
#         # print(str(vertex), end="\n")
#         urutan.append(str(vertex))
#             # If not visited, mark it as visited, and
#             # enqueue it
        
#         for tetangga in dictGraph[vertex]:
#             # print("neighbor:",tetangga)
#             if tetangga not in visited:
#                 gnthisneighbor = dictGraph[vertex].index(tetangga)
#                 nilaif = fn(dictGraphCost[vertex][gnthisneighbor], dictH[tetangga])
                
#                 # print("nilaif:", nilaif)
#                 visited.add(tetangga)
#                 queue.append(tetangga)
    
#     # print('visited:', visited)
#     if tujuan not in urutan:
#         print(asal,"&",tujuan,"tidak terhubung.")
#     else:
#         for x in urutan:
#             print(x, end =' ')
#     print("")

def astar(dictGraph, dictH, asal, tujuan, dictGraphCost):
    opened = []
    closed = []
    opened.append(asal)
    print(opened)
    i = 0
    nilaign = 0
    nilaifn = []
    for j in range(len(dictGraphCost[opened[0]])):
        nilaifn.append(fn(dictGraphCost[opened[0]][j],dictH[dictGraph[opened[0]][j]]))
    # print("nilaifn:", nilaifn)

    while opened != tujuan and i <= len(dictGraph):
        # print("nilaian", dictGraph[opened[0]])
        minfn = nilaifn.index(min(nilaifn))
        # print("minfn:",minfn)
        nilaign += nilaifn[minfn]
        selanjutnya = dictGraph[opened[0]][minfn]
        # print("Closed:",closed)
        if selanjutnya in closed:
            nilaifn.pop(dictGraph[opened[0]].index(selanjutnya))
            dictGraph[opened[0]].pop(dictGraph[opened[0]].index(selanjutnya))
            minfn = nilaifn.index(min(nilaifn))
            selanjutnya = dictGraph[opened[0]][minfn]
        # print("selanjutnya:",selanjutnya)
        curr = opened.pop(0)
        # print("curr:",curr)
        closed.append(curr)
        opened.append(selanjutnya)
        # print("o:",opened)
        if curr == tujuan:
            break
        else:
            i += 1
            nilaifn = []
            for j in range(len(dictGraphCost[opened[0]])):
                nilaifn.append(fn(nilaign,dictH[dictGraph[opened[0]][j]]))
            # print("nilaifn:", nilaifn)
    return closed



# main program
if __name__ == '__main__':
    
    namaFile = "../test/itb1.txt"
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
    # print("dictgraph:", dictGraph) #'Bahasa': ['Perpus', 'CIBE']
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
    # print("dictH:",dictH)

    # bfs(dictGraph, asal, tujuan)
    # print("\n----------------")
    # astar1(dictGraph,asal,tujuan,dictH,arrVertex)
    # print("----------------")
    astar(dictGraph,dictH,asal,tujuan,dictGraphCost)