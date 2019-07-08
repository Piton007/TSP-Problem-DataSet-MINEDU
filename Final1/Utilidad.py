from CCity import *
from math import radians, cos, sin, asin, sqrt


def alterar_recorrido(recorrido):
        #Funcion recursiva que retorna el tour mejorado
        distancia_original = longitud_recorrido(recorrido)
        for (inicio, fin) in segmentos(len(recorrido)):
            revertir(recorrido, inicio, fin)
        #Si no ha mejorado llama denuevo a la funcion
        if longitud_recorrido(recorrido) < distancia_original:
            return alterar_recorrido(recorrido)
        return recorrido
    
def segmentos(N):
        #Genera todos los segmentos
        return [(inicio, inicio + tamaño)
                for tamaño in range(N, 2-1, -1)
                for inicio in range(N - tamaño + 1)]
    
def revertir(recorrido, i, j):
        A, B, C, D = recorrido[i-1], recorrido[i], recorrido[j-1], recorrido[j % len(recorrido)]
        if distance(A, B) + distance(C, D) > distance(A, C) + distance(B, D):
            recorrido[i:j] = reversed(recorrido[i:j])
def recorrido_corto(recorridos): 
        return min(recorridos, key=longitud_recorrido)
def longitud_recorrido(recorrido):
        return sum(distance(recorrido[i],recorrido[i-1]) for i in range(len(recorrido)))
    
def distance(A,B):
        lat1,lat2,lon1,lon2=A.y,B.y,A.x,B.x
        R = 6372.8 #km
        dLat = radians(abs(lat2 - lat1))
        dLon = radians(abs(lon2 - lon1))
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(a))
        return R * c
    
def Tour(tour):
        return list(tour)
