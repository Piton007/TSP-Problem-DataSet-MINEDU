from Utilidad import *


class Divide_Conquitaras:
    
    def __init__(self,cities):
        self.Tour=self.Execute(cities)
        
    def length(self):
        return longitud_recorrido(self.Tour)
    
    def rotar(self,secuencia):
        
        return [secuencia[i:] + secuencia[:i] for i in range(len(secuencia))]
    
    def combinar_recorridos(self,recorrido1, recorrido2):
        segmento1, segmento2 = self.rotar(recorrido1), self.rotar(recorrido2)
        recorridos = [s1 + s2 for s1 in segmento1 for s  in segmento2 for s2 in (s, s[::-1])]
        return recorrido_corto(recorridos)
    
    def dividir_ciudades(self,cities):
            anchura, altura = self.distancia_puntos([c.x for c in cities]), self.distancia_puntos([c.y for c in cities])
            Key = 'x' if (anchura > altura) else 'y'
            cities = sorted(cities, key=lambda c: getattr(c,Key))
            mitad = len(cities) // 2
            return frozenset(cities[:mitad]), frozenset(cities[mitad:])
        
    def dq_tsp(self,cities):
        if len(cities) <= 3:
            return list(cities)
        else:
            Cs1, Cs2 = self.dividir_ciudades(cities)
            return self.combinar_recorridos(self.dq_tsp(Cs1), self.dq_tsp(Cs2))
       
        
    def distancia_puntos(self,puntos): return max(puntos) - min(puntos)
    
    
    def Execute(self,cities):
        tour=self.dq_tsp(cities)
        tour+=[tour[0]]
        return tour
    



    


