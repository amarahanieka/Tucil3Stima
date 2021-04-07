# tucil3 :""""))
import math
import networkx as nx 
import matplotlib.pyplot as plt

def readFile(namaFile):
    arrFile = []
    openFile = open(namaFile, 'r')
    readFile = openFile.readlines()
    for line in readFile:
        each = line.rstrip('\n')
        arrFile.append(each)
    return arrFile

def euclideanDistance(titika, titikb):
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
            arrCoordinate[i][j] = float(arrCoordinate[i][j])
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

def astar(dictGraph, dictH, asal, tujuan, dictGraphCost):
    opened = []
    closed = []
    opened.append(asal)
    i = 0
    nilaign = 0
    nilaifn = []
    for j in range(len(dictGraphCost[opened[0]])):
        nilaifn.append(fn(dictGraphCost[opened[0]][j],dictH[dictGraph[opened[0]][j]]))
    curr = ''
    while not (curr == tujuan):
        if (len(nilaifn) > 1):
            minfn = nilaifn.index(min(nilaifn))
        else:
            minfn = 0
        nilaign += dictGraphCost[opened[0]][minfn]
        selanjutnya = dictGraph[opened[0]][minfn]
        if selanjutnya in closed:
            nilaifn.pop(dictGraph[opened[0]].index(selanjutnya))
            hei = dictGraph[opened[0]].pop(dictGraph[opened[0]].index(selanjutnya))
            if (len(nilaifn) > 1):
                minfn = nilaifn.index(min(nilaifn))
                selanjutnya = dictGraph[opened[0]][minfn]
            else:
                selanjutnya = hei
        curr = opened.pop(0)
        closed.append(curr)
        opened.append(selanjutnya)
        if curr == tujuan:
            break
        else:
            try:
                raise ValueError 
            except (ValueError,IndexError):
                pass
            i += 1
            nilaifn = []
            try:
                for j in range(len(dictGraphCost[opened[0]])):
                    nilaifn.append(fn(nilaign,dictH[dictGraph[opened[0]][j]]))
            except IndexError:
                # print("an index error!")
                break
    if tujuan in closed:
        return closed
    else:
        return None

def deg2rad(deg):
    return deg * (math.pi/180)

def jarakdalamkm(lat1,lon1,lat2,lon2):
  R = 6371; #Radius of the earth in km
  dLat = deg2rad(lat2-lat1);  #deg2rad below
  dLon = deg2rad(lon2-lon1); 
  a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)); 
  d = R * c #Distance in km
  return d

def redEdges(hasil):
    newHasil2 = []
    for i in range(len(hasil)):
        if (i != 0):
            newHasil2.append(hasil[i])

    newHasil1 = []
    for i in range(len(hasil)-1):
        newHasil1.append(hasil[i])
    red_edges1 = list(zip(newHasil1,newHasil2))
    red_edges2 = list(zip(newHasil2,newHasil1))
    for i in range(len(red_edges2)):
        red_edges1.append(red_edges2[i])
    return red_edges1


# main program
if __name__ == '__main__':
    out = False
    
    filegraf = input("Masukkan nama file graf tanpa extension: ")
    namaFile = "../test/"+filegraf+".txt"
    arrFile = readFile(namaFile)

    while (out != True):
        

        #prep
        arrVertexCoordinate = vertexCoordinate(arrFile)
        arrVertex = makeListVertex(arrFile)
        listtempat = set(arrVertex)
        arrMatrix = makeMatrix(arrFile)
        dictGraph = makeGraph(arrMatrix, arrVertex)
        dictGraphCost = makeGraphCost(arrMatrix, arrVertex, arrVertexCoordinate)

        asal = input("Masukkan lokasi asal: ")
        while asal not in listtempat:
            print("Tempat tidak tersedia. Masukkan tempat yang sesuai.")
            asal = input("Masukkan lokasi asal: ")

        tujuan = input("Masukkan lokasi tujuan: ")
        while tujuan not in listtempat:
            print("Tempat tidak tersedia. Masukkan tempat yang sesuai.")
            tujuan = input("Masukkan lokasi tujuan: ")
        
        dictH = heu(arrVertex, tujuan)

        hasil = astar(dictGraph,dictH,asal,tujuan,dictGraphCost)
        jarak = 0
        if (hasil != None):
            for i in range(len(hasil)-1):
                jarak += jarakdalamkm(arrVertexCoordinate[hasil[i]][0],arrVertexCoordinate[hasil[i]][1],arrVertexCoordinate[hasil[i+1]][0], arrVertexCoordinate[hasil[i+1]][1])
            print(*hasil, sep =' -> ')
            print("Jarak:", jarak,"km")
            g = nx.Graph()
            for i in dictGraph:
                for j in range(len(dictGraph[i])):
                    g.add_edge(i, dictGraph[i][j], weight=dictGraphCost[i][j])

            red_edges = redEdges(hasil)
            edge_colors = ['black' if not edge in red_edges else 'red' for edge in g.edges()]
            nx.draw(g, edge_color = edge_colors, with_labels = True)
            plt.show()
        else:
            print("Kedua tempat tidak terhubung.")
        print("")
        lagi = input("Ingin mencoba kembali? Y/N: ")
        while (lagi != "Y" and lagi != "N"):
            lagi = input("Input anda salah! Masukan Y/N: ")
        if (lagi == "Y"):
            filegraf = input("Masukkan nama file graf tanpa extension: ")
            namaFile = "../test/"+filegraf+".txt"
            arrFile = readFile(namaFile)
        elif (lagi == "N"):
            print("Terima kasih sudah menggunakan layanan kami!")
            out = True
            
            
