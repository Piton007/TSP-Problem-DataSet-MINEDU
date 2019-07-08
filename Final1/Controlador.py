import json
import functools
import time
from CCity import *
from Utilidad import *
class TSP:
    
    def __init__(self,geojson,tipo,IE=False,DIST="CHORRILLOS"):
        #Carga Departamental por defecto
        self.json=geojson
        self.Data=[]
        if IE:
            self.load_data_ie(DIST)
        else:
            self.load_data(tipo)
        
    def load_data(self,capital):
        self.Data=[]
        with open(self.json,'r',encoding='utf8') as contenido:
            data=json.load(contenido)
            for p in data['features']:
                if p['properties']['CAPITAL']==str(capital):
                    self.Data.append(City(p['geometry']['coordinates'][0],p['geometry']['coordinates'][1],p['properties']['NOMCP']))
    def load_data_ie(self,DIST,DEP="LIMA",PROV="LIMA"):
        CPCOD=[]
        with open("fuente.json",'r',encoding='utf8') as file:
            data=json.load(file)
            for feature in data['features']:
                if feature['properties']['DEP']==DEP and  feature['properties']['PROV']==PROV and feature['properties']['DIST']==DIST and feature['properties']['CON_IE']=="1":
                    CPCOD+=[feature['properties']['CODCP']]
            file.close()
        for cp in CPCOD:
            self.institutos(cp)
    def institutos(self,CODCP):
        with open("IE_P.json",'r',encoding='utf8') as file:
            data=json.load(file)
            for feature in data['features']:
                if feature['properties']['CODCPSIG']==CODCP:
                    self.Data+=[City(feature['geometry']['coordinates'][0],feature['geometry']['coordinates'][1],feature['properties']['CEN_EDU_L'])]
            file.close()
            


    #@functools.lru_cache(None)
    def Execute_Algorithms(self,algoritmo,mejora=False):
        
        #Ejecuta cualquier algoritmo para TSP
        t0=time.perf_counter()
        tour= algoritmo(self.Data)
        tour.Tour=alterar_recorrido(tour.Tour) if mejora==True else tour.Tour
        t1=time.perf_counter() 
        assert self.validar_recorrido(tour.Tour),"Esto no es una ruta permita"
        #print("{} city tour with length {:.1f} in {:.3f} secs for {}".format(len(tour.Tour), tour.length(),t1-t0  , tour.__class__.__name__))
        valores={"Ciudades":len(tour.Tour)-1,"Longitud":"{:.3f}".format(tour.length()),"Tiempo":"{0:.4f}".format(t1-t0),"Tour":tour.Tour}
        return valores
    
    
    def validar_recorrido(self,tour):
        return set(tour)==set(self.Data) and len(tour)-1==len(self.Data)
    


                



