from Utilidad import *
from itertools import combinations

def find(v, nodo):
        
        if v[nodo]<0:
            
            return nodo
        else:
            padre = find(v, v[nodo])
            return padre
def union(v, a, b):
    pa = find(v, a)
    pb = find(v, b)
    if pa == pb: return    
    if v[pa] <= v[pb]:
        v[pa] += v[pb]
        v[pb] = pa
    elif v[pb] < v[pa]:
        v[pb] += v[pa]
        v[pa] = pb

class Arista:
    def __init__(self,A,B):
        self.inicio=A
        self.fin=B
        self.peso=distance(A[0],B[0])

class Grafo:
    def __init__(self,cities):
        self.cities=[]
        self.aristas=[]
        self.GenerarIndices(cities)
        self.GenerarAristas()
    def GenerarIndices(self,cities):
        for i in range(len(cities)):
            self.cities+=[(cities[i],i)]
        
    def GenerarAristas(self):
        duplas=combinations(self.cities,2)
        
        for i in list(duplas):
            arista=Arista(i[0],i[1])
            self.aristas+=[arista]
        
class Kruskal:
    def __init__(self,data):
        self.grafo=Grafo(data)
        self.Tour=[]
        self.Generar_Arbol()
    def Generar_Arbol(self):
        aristas=sorted(self.grafo.aristas,key=lambda edge:edge.peso)
        QUVector=[-1]*len(self.grafo.cities)
        while len(aristas)>0:
            arista_sel=aristas[0]
            if self.CompararRaices(arista_sel.inicio[1],arista_sel.fin[1],QUVector):
                
                union(QUVector, arista_sel.inicio[1], arista_sel.fin[1])
            aristas.remove(arista_sel)
        origen=""
        for nodo in range(len(QUVector)):
            if QUVector[nodo]<0:
                origen=nodo
        tour=[]
        self.Generar_PreOrderT(origen,QUVector,tour)
        tour+=[tour[0]]
        for i in tour:
            for nodo in self.grafo.cities:
                if nodo[1]==i:
                    self.Tour+=[nodo[0]]
                    break
        
    def CompararRaices(self,a,b,v):
        if find(v, b) != find(v, a):
            return True
        return False
    def Generar_PreOrderT(self,padre,v,tour):
        tour+=[padre]
        for i in range(len(v)):
            if v[i]==padre:
                self.Generar_PreOrderT(i,v,tour)
                
                
    def length(self):
        return longitud_recorrido(self.Tour)
               



          
    
        
        
        
        
        

        
        
        
    
