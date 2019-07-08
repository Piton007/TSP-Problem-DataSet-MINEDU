from Utilidad import *

class Neighbor():
    
    def __init__(self,cities):
        self.Tour=self.Execute(cities)
        
    def length(self):
        return longitud_recorrido(self.Tour)

    def Algorithm(self,inicio,cities):

        tour=[inicio]
        no_visitado=[ city for city in cities if city!=inicio]
        while no_visitado:
            actual=self.Cercano(tour[-1],no_visitado)
            tour.append(actual)
            no_visitado.remove(actual)
        tour.append(inicio)
        return tour
    def Cercano(self,actual,no_visitado):
        return min(no_visitado, key=lambda c:distance(c,actual))

    def Execute(self,cities):
        return recorrido_corto([self.Algorithm(inicio,cities) for inicio in cities])
