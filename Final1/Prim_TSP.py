from Utilidad import *
from itertools import combinations

class Arista:
    def __init__(self,A,B):
        self.inicio=A
        self.fin=B
        self.peso=distance(A,B)

class Grafo:
    def __init__(self,cities):
        self.cities=cities
        self.aristas=[]
        self.GenerarAristas()
    def GenerarAristas(self):
        duplas=combinations(self.cities,2)
        for i in list(duplas):
            arista=Arista(i[0],i[1])
            self.aristas+=[arista]
class Prim:
    def __init__(self,data):
        self.grafo=Grafo(data)
        self.arbol=self.Generar_Arbol()
        self.Tour=[]
        self.Generar_PreOrderT(self.grafo.cities[0])
        self.Tour+=[self.Tour[0]]
    def Generar_Arbol(self):
        arbol={self.grafo.cities[0]:[]}
        aristas=sorted(self.grafo.aristas,key=lambda edge:edge.peso)
        while len(arbol)<len(self.grafo.cities):
            padre,hijo=self.Sel_Arista(aristas,arbol)
            arbol[padre]+=[hijo]
            arbol[hijo]=[]
        return arbol
    def Sel_Arista(self,aristas,arbol):
        list_aristas=[arista for arista in aristas if (arista.inicio in arbol)^(arista.fin in arbol)]
        padre,hijo=list_aristas[0].inicio,list_aristas[0].fin
        aristas.remove(list_aristas[0])
        return (padre,hijo) if (padre in arbol) else (hijo,padre)
    def Generar_PreOrderT(self,padre):
        self.Tour+=[padre]
        if len(self.arbol[padre])<1:
            return 
        else:
            for hijo in self.arbol[padre]:
                self.Generar_PreOrderT(hijo)
    def length(self):
        return longitud_recorrido(self.Tour)
               
            
    
        
        
        
        
        

        
        
        
    
