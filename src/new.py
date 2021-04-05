class Vertex:
    def __init__(self, nama):
        self.nama = nama
        self.adj = {}

    def __str__(self):
        return str([x.nama for x in self.adj])
    
    def getnamavertex(self):
        return self.nama

    def add_neighbor(self, neighbor, jarak):
        self.adj[neighbor] = jarak
    
    def getconnections(self):
        return self.adj.keys()  

    def getjarak(self, neighbor):
        return self.adj[neighbor]

class Graph:
    def __init__(self, jumlahvertex):
        self.vertices = {}
        self.jumlahvertex = jumlahvertex
    
    def __iter__(self):
        return iter(self.vertices.values())
    
    def addvertex(self, nama):
        vertexbaru = Vertex(nama)
        self.vertices[nama] = vertexbaru
        return vertexbaru

    def getvertices(self):
        return self.vertices.keys()

    def add_edge(self, asal, tujuan, cost):
        # if asal not in self.vertices:
        #     self.addvertex(asal)
        # if tujuan not in self.vertices:
        #     self.addvertex(tujuan)

        self.vertices[asal].add_neighbor(self.vertices[tujuan], cost)
        # self.vertices[tujuan].add_neighbor(self.vertices[asal], cost)
    

#main program
if __name__ == '__main__':
    file = open('../test/tes.txt', 'r')
    fileawal = []
    for row in file:
        fileawal.append([str(x) for x in row.split()])
    convertbarisawal = list(map(int,fileawal[0]))

    banyakvertex = convertbarisawal[0]
    # print(banyakvertex)

    namatempat = [baris[0] for baris in fileawal[1:banyakvertex+1]]
    #print(namatempat)

    listkoordinat = [baris[1:3] for baris in fileawal[1:banyakvertex+1]]
    # ubah jadi integer
    for i in range(len(listkoordinat)):
        for j in range(2):
            listkoordinat[i][j] = int(listkoordinat[i][j])
    # print(listkoordinat)

    adjmatfile = [baris[0:8] for baris in fileawal[banyakvertex+1:banyakvertex+1+banyakvertex]]
    for i in range(banyakvertex):
        for j in range(banyakvertex):
            adjmatfile[i][j] = int(adjmatfile[i][j])
    # print(adjmatfile)

    # bikin graf
    g = Graph(banyakvertex)
    for i in range(banyakvertex):
        g.addvertex(namatempat[i])

    # print semua vertex
    for v in g:
        print ('Vertex %s' %(v.getnamavertex()))
    

    for i in range(banyakvertex):
        for j in range(banyakvertex):
            if(adjmatfile[i][j] == 1):
                cost = (((listkoordinat[i][0]-listkoordinat[j][0])**2)+((listkoordinat[i][1]-listkoordinat[j][1])**2))**0.5
                g.add_edge(namatempat[i],namatempat[j],cost)
                # print("Koordinat:", listkoordinat[i], "->", listkoordinat[j])
                # print(namatempat[i],"->",namatempat[j], ". Cost:", cost)
    
    # for v in g:
    #     # print(g)
    #     # print ('Vertex %s' %(v.getnamavertex()))
    #     print ('Vertex %s punya tetangga %s' %(v.getnamavertex, g.vertices[v.getnamavertex()]))

    for v in g:
        for w in v.getconnections():
            print ('(%s, %s, %f)'  % (v.getnamavertex(), w.getnamavertex(), v.getjarak(w)))
    
    for v in g:
        print ('Vertex %s tetanggaan sama %s' %(v.getnamavertex(), g.vertices[v.getnamavertex()]))
    
    #akses tetangga A
    tetangga = g.vertices['A']
    print(tetangga)