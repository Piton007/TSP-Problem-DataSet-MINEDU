from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from CCity import *

xs=[]
ys=[]
m=None
area=None


def BaseMap(Area,Data,title=""):
    global xs,ys,m,area
    area=Area
    m = Basemap(projection='mill',
                llcrnrlat = -20,
                llcrnrlon = -86,
                urcrnrlat = 0,
                urcrnrlon = -60,
                resolution='l',ax=Area)
    
    for i,city in enumerate(Data):
        xpt,ypt=m(city.x,city.y)
        
        
        xs+=[xpt]
        ys+=[ypt]
    
    return m

def Plot(Basemap,Tour):
    
    global xs,ys,m,area
    
    Basemap.drawcoastlines()
    
    Basemap.bluemarble()
    
    
    
    Basemap.drawcountries(linewidth=1)
    
    Basemap.drawstates(color='b')

    #Basemap.plot(xs,ys,'y*',markersize=8)   
    xs=[]
    ys=[]
    
    for i,city in enumerate(Tour):
        xpt,ypt=Basemap(city.x,city.y)
        
            
        if i<len(Tour)-1 and i>0 :    
            area.text(xpt, ypt,i, bbox=dict(facecolor='yellow', alpha=0.5,pad=2),fontsize=7)
        xs+=[xpt]
        ys+=[ypt]
        if i==0:
            area.text(xpt, ypt,i, bbox=dict(facecolor='red', alpha=0.5),fontsize=7)
    
    #Basemap.plot(xs[0],ys[0],'r*',markersize=10,label="")
    Basemap.plot(xs,ys,linewidth=2,label='DQ',color='r')

   
    #Basemap.shadedrelief()
    #Basemap.fillcontinents()
    #Basemap.etopo()
    #Basemap.drawgreatcircle(ArequipaLon,ArequipaLat,LimaLon,LimaLat,linewidth=1,color='c')
    #plt.legend(loc=4)
    #plt.title('Geolocalizacion')
    #plt.show()
    

