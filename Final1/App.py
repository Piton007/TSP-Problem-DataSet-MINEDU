from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import basemap as Bm
from Controlador import *
from AlgoritmDV import Divide_Conquitaras as DQ
from NN_TSP import Neighbor as NB
from Prim_TSP import Prim
from Kruskal_TSP import Kruskal

def Estilos():
    style=ttk.Style()
    style.theme_use("alt")
    style.configure("TFrame",background="gray38")
    style.configure("TLabel",font="Arial 16",anchor=CENTER,width=9,background="gray38",foreground="white")
    style.configure("H1.TLabel",font="Arial 32 bold",anchor="center",width=14)
    style.configure("H2.TLabel",font="Arial 28 ",anchor="center",width=14)
    style.configure("TButton",font="Arial 20 bold",anchor="center",foreground="white",background="red")
    style.configure("Ejecutar.TButton",font="Arial 20 bold",anchor="center",foreground="white",padding=(25,10),width=8,background="red")
    style.configure("TMenubutton",font="Arial 12",anchor="center",width=17)
    
    return style

    
class FRutas():
    def __init__(self,root,ruta):
        self.root=root
        self.ruta=ruta
        self.root.title("Ruta")
        self.root.resizable(width=False,height=False)
        self.root.iconbitmap('Icono.ico')
        self.CrearComponentes()
        self.CrearWidgets()

    
    def CrearComponentes(self):
        self.Clb1=ttk.Frame(self.root,borderwidth=2,relief="raised")
        self.Clb2=ttk.Frame(self.root,borderwidth=2,relief="raised")
        self.Clb3=ttk.Frame(self.root,borderwidth=2,relief="raised")
        self.CbtnReturn=ttk.Frame(self.root,borderwidth=2,relief="raised")
        self.Clb1.grid(column=0,row=0,sticky=(W,E,N,S),ipadx=10,ipady=10)
        self.Clb2.grid(column=1,row=0,sticky=(W,E,N,S),ipadx=10,ipady=10)
        self.Clb3.grid(column=2,row=0,sticky=(W,E,N,S),ipadx=10,ipady=10)
        self.CbtnReturn.grid(column=0,row=1,columnspan=3,sticky=(W,E,N,S),ipadx=10,ipady=10)
        
        
        
    def CrearWidgets(self):
        cont=(len(self.ruta)-1)//3
        scrollbar1=Scrollbar(self.Clb1, orient="vertical")
        lb1=Listbox(self.Clb1, width=30,height=6,font=("Helvetica", 12),yscrollcommand=scrollbar1.set)
        lb1.pack(side="left", fill="y")
        scrollbar1.pack(side="right", fill="y")
        scrollbar1.config(command=lb1.yview)
        self.LlenarListBox(lb1,0,cont)
        scrollbar2=Scrollbar(self.Clb2, orient="vertical")
        lb2=Listbox(self.Clb2, width=30,height=6,font=("Helvetica", 12),yscrollcommand=scrollbar2.set)
        lb2.pack(side="left", fill="y")
        scrollbar2.pack(side="right", fill="y")
        scrollbar2.config(command=lb2.yview)
        self.LlenarListBox(lb2,cont,(cont+(len(self.ruta)-1)//3))
        cont=cont+((len(self.ruta)-1)//3)
        scrollbar3=Scrollbar(self.Clb3, orient="vertical")
        lb3=Listbox(self.Clb3, width=30,height=6,font=("Helvetica", 12),yscrollcommand=scrollbar3.set)
        lb3.pack(side="left", fill="y")
        scrollbar3.pack(side="right", fill="y")
        scrollbar3.config(command=lb3.yview)
        self.LlenarListBox(lb3,cont,len(self.ruta)-1)
        self.btnruta=ttk.Button(self.CbtnReturn,command=self.root.destroy,text="Regresar",width=12)
        self.btnruta.pack(fill="none", expand=True)
        
    def LlenarListBox(self,lbox,inicio,fin):
        for i in range(inicio,fin):
                lbox.insert(END,str(i)+"-->"+self.ruta[i].nombre)
            
            
        
         
        

class FPrincipal():
    def __init__(self,fuente="fuente.json"):
        self.bd=fuente
        self.root=Tk()
        self.root.title("TSP")
        self.root.iconbitmap('Icono.ico')
        self.root.resizable(width=True,height=True)
        self.style=Estilos()
        self.Algoritmos=["Vecino Cercano","DV","VC plus","DV plus","Prim","Prim plus","Kruskal","Kruskal Plus"]
        self.TipoData=["Departamental","Provincial","Distrital","Centros Poblados","Centro Educativo"]
        self.ruta=None
        self.algoritmo=StringVar()
        self.data=StringVar()
        self.longitud=StringVar()
        self.tiempo=StringVar()
        self.ciudades=StringVar()
        self.algoritmo.set(self.Algoritmos[0])
        self.data.set(self.TipoData[0])
        self.canvas=ttk.Frame(self.root)
       
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.canvas.grid(row=0,column=0,sticky=(N,S,W,E))
        self.canvas.columnconfigure(0,weight=1)
        self.canvas.columnconfigure(1,weight=1)
        self.canvas.columnconfigure(2,weight=1)
        self.canvas.columnconfigure(3,weight=1)
        self.canvas.rowconfigure(0,weight=1)
        self.canvas.rowconfigure(1,weight=1)
        self.canvas.rowconfigure(2,weight=1)
        self.canvas.rowconfigure(3,weight=1)
        self.canvas.rowconfigure(4,weight=1)
        self.canvas.rowconfigure(5,weight=1)
        self.canvas.rowconfigure(6,weight=1)
        self.canvas.rowconfigure(7,weight=1)
        self.canvas.rowconfigure(8,weight=1)
        self.canvas.rowconfigure(9,weight=1)
        self.CrearComponentes()
        self.GenerarWidgets()
        self.GenerarMapa()
        
    def GenerarDetalle(self):
        new_root=Toplevel()
        Dialog=FRutas(new_root,self.ruta)
    def GenerarMapa(self):
        
        data_sel=self.data.get()
        algoritmo_sel=self.algoritmo.get()
        data=None
        info=None
        if self.TipoData.index(data_sel)==0:
            data=TSP(self.bd,1)
        if self.TipoData.index(data_sel)==1:
            data=TSP(self.bd,2)
        if self.TipoData.index(data_sel)==2:
            data=TSP(self.bd,3)
        if self.TipoData.index(data_sel)==3:
            data=TSP(self.bd,0)
        if self.TipoData.index(data_sel)==4:
            data=TSP(self.bd,0,True)
        if self.Algoritmos.index(algoritmo_sel)==0:
            info=data.Execute_Algorithms(NB)
        if self.Algoritmos.index(algoritmo_sel)==1:
            info=data.Execute_Algorithms(DQ)
        if self.Algoritmos.index(algoritmo_sel)==2:
            info=data.Execute_Algorithms(NB,True)
        if self.Algoritmos.index(algoritmo_sel)==3:
            info=data.Execute_Algorithms(DQ,True)
        if self.Algoritmos.index(algoritmo_sel)==4:
            info=data.Execute_Algorithms(Prim)
        if self.Algoritmos.index(algoritmo_sel)==5:
            info=data.Execute_Algorithms(Prim,True)
        if self.Algoritmos.index(algoritmo_sel)==6:
            info=data.Execute_Algorithms(Kruskal,True)
        if self.Algoritmos.index(algoritmo_sel)==7:
            info=data.Execute_Algorithms(Kruskal,True)
        
        figure=Figure(figsize=(5,4),dpi=100)
        subplot=figure.add_subplot(111)
        mapa=Bm.BaseMap(subplot,data.Data)
        self.ruta=info["Tour"]
        Bm.Plot(mapa,self.ruta)
        self.longitud.set(info["Longitud"]+str(" km"))
        self.tiempo.set(info["Tiempo"]+str(" s"))
        self.ciudades.set(str(info["Ciudades"])+str(" ciudades"))
        for widget in self.Basemap.winfo_children():
            widget.destroy()
        canvasplot=FigureCanvasTkAgg(figure,master=self.Basemap)
        canvasplot.draw()
        canvasplot.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        toolbar= NavigationToolbar2Tk(canvasplot,self.Basemap)
        toolbar.update()
        figure.tight_layout(pad=0, w_pad=0, h_pad=0)
          
        
        
            
            
    def CrearComponentes(self):
        
        self.CTitulo=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.Basemap=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.ClblTipo=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.ClblAlg=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.CsbAlg=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.CsbTipo=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.CExec=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.ClblInfo=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.ClblLon=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.ClblTime=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.ClblCity=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.CbtnRuta=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.CinpLon=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.CinpCity=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
        self.CinpTime=ttk.Frame(self.canvas,borderwidth=2,relief="raised")
    
        self.CTitulo.grid(column=0,row=0,columnspan=4,sticky=(W,E,N,S))
        self.ClblTipo.grid(row=1,column=0,sticky=(W,E,N,S))
        self.ClblAlg.grid(row=2,column=0,sticky=(W,E,N,S))
        self.CsbAlg.grid(row=2,column=1,sticky=(W,E,N,S),ipadx=10,ipady=10)
        self.CsbTipo.grid(row=1,column=1,sticky=(W,E,N,S),ipadx=10,ipady=10)
        self.CExec.grid(row=1,column=2,rowspan=2,sticky=(W,E,N,S),ipadx=10)
        self.ClblInfo.grid(row=1,column=3,rowspan=2,sticky=(W,E,N,S),ipadx=10)
        self.ClblLon.grid(row=3,column=3,sticky=(W,E,N,S))
        self.ClblTime.grid(row=5,column=3,sticky=(W,E,N,S))
        self.ClblCity.grid(row=7,column=3,sticky=(W,E,N,S))
        self.CinpLon.grid(row=4,column=3,sticky=(W,E,N,S))
        self.CinpTime.grid(row=6,column=3,sticky=(W,E,N,S))
        self.CinpCity.grid(row=8,column=3,sticky=(W,E,N,S))
        self.CbtnRuta.grid(row=9,column=3,sticky=(W,E,N,S))
        self.Basemap.grid(row=3,column=0,sticky=(W,E,N,S),columnspan=3,rowspan=7)
        #self.CLbDetails=ttk.Frame(self.canvas,borderwidth=4,relief="solid")   
    def GenerarWidgets(self):
        self.btnejecutar=ttk.Button(self.CExec,command=self.GenerarMapa,text="Ejecutar",style="Ejecutar.TButton")
        self.lbltitle=ttk.Label(self.CTitulo,text="TSP PROBLEM",style="H1.TLabel")
        self.lbltipo=ttk.Label(self.ClblTipo,text="Tipo:",style="TLabel")
        self.lblalgoritmo=ttk.Label(self.ClblAlg,text="Algoritmo:",style="TLabel")
        self.omtipo=ttk.OptionMenu(self.CsbTipo,self.data,self.data.get(),*self.TipoData,style="TMenubutton")
        self.omalgoritmo=ttk.OptionMenu(self.CsbAlg,self.algoritmo,self.algoritmo.get(),*self.Algoritmos,style="TMenubutton")
        self.lblinfo=ttk.Label(self.ClblInfo,text="INFORMACION",style="H2.TLabel")
        self.lblLongitud=ttk.Label(self.ClblLon,text="Longitud")
        self.lblTiempo=ttk.Label(self.ClblTime,text="Tiempo")
        self.lblCiudades=ttk.Label(self.ClblCity,text="Ciudades")
        self.inpLongitud=ttk.Entry(self.CinpLon,textvariable=self.longitud,state=DISABLED,font="Arial 18 bold",justify=CENTER,width=14)
        self.inpTiempo=ttk.Entry(self.CinpTime,textvariable=self.tiempo,state=DISABLED,font="Arial 18 bold",justify=CENTER,width=14)
        self.inpCiudades=ttk.Entry(self.CinpCity,textvariable=self.ciudades,state=DISABLED,font="Arial 18 bold",justify=CENTER,width=14)
        self.btnruta=ttk.Button(self.CbtnRuta,command=self.GenerarDetalle,text="Ruta",width=11)
        self.btnejecutar.pack(fill="none", expand=True)
        self.lbltitle.pack(fill="none", expand=True)
        self.lbltipo.pack(fill="none", expand=True)
        self.lblalgoritmo.pack(fill="none", expand=True)
        self.omtipo.pack(fill="none", expand=True)
        self.omalgoritmo.pack(fill="none", expand=True)
        self.lblinfo.pack(fill="none", expand=True)
        self.lblLongitud.pack(fill="none", expand=True)
        self.lblTiempo.pack(fill="none", expand=True)
        self.lblCiudades.pack(fill="none", expand=True)
        self.inpLongitud.pack(fill="none", expand=True)
        self.inpTiempo.pack(fill="none", expand=True)
        self.inpCiudades.pack(fill="none", expand=True)
        self.btnruta.pack(fill="none", expand=True)
        
        
    
        
    

def main():
    app=FPrincipal()
    app.root.mainloop()
    return 0
#Sirve para ejecutar el modulo actual como principal
if __name__=='__main__':
    main()
    
