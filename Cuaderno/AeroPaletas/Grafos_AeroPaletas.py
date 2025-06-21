import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import random
import json
from collections import deque

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class Aeropuertos_1:
    def __init__(self):
        self.g = nx.DiGraph()
    
    def cargar_J(self):
        with open("AeroPaletas/Json/Info.json") as f:
            self.info=json.load(f)
        
        with open("AeroPaletas/Json/Aero.json") as x:
            self.Aero=json.load(x) 
        
    def crear_nodos(self):
        self.lisD=[]
        for nombre, datos in self.info.items():
            nodo_destino = f"Nombre: {nombre}\nCosto: {datos['Costo de Hospedaje']}\nRecomendable: {datos['Recomendable']}"
            self.lisD.append(nodo_destino)
        self.g.add_nodes_from(self.lisD)

    def crear_conexiones(self):
        l = self.Aero
        if not l:
            print("Error: No se encontraron aerolíneas en Aero.json")
            return

        x = random.randrange(10, 15)
        for y in range(x):
            aerolinea = random.choice(l)
            noRam1 = random.choice(self.lisD) 
            noRam2 = random.choice(self.lisD)

            while noRam1 == noRam2:
                noRam2 = random.choice(self.lisD)

            peso = random.randint(100, 1000)
            self.g.add_edge(noRam1, noRam2, weight=peso, airline=aerolinea)

    def bfs(self, inicio):
        if inicio not in self.g:
            print(f"Error: El nodo '{inicio}' no existe en el grafo.")
            return []

        visitados = set()
        cola = deque([inicio])
        recorrido = []

        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                vecinos = list(self.g.successors(nodo))
                cola.extend([vecino for vecino in vecinos if vecino not in visitados])

        return recorrido

    def ruta_mas_corta(self, inicio, destino):
        try:
            camino = nx.shortest_path(self.g, source=inicio, target=destino, weight="weight")
            return camino
        except nx.NetworkXNoPath:
            messagebox.showinfo("","No hay ruta disponible entre los nodos seleccionados.")
            return []

    def mostrar(self, ruta_destacada=None):
        pos = nx.spring_layout(self.g)

        nx.draw(self.g, pos, with_labels=True, font_color='black', node_color='#A569BD', node_size=500, font_size=8, arrows=True)
        
        edge_labels = {(u, v): f"{d['airline']}" for u, v, d in self.g.edges(data=True)}
        nx.draw_networkx_edge_labels(self.g, pos, edge_labels=edge_labels)

        if ruta_destacada:
            path_edges = list(zip(ruta_destacada, ruta_destacada[1:]))
            nx.draw_networkx_edges(self.g, pos, edgelist=path_edges, edge_color="red", width=2)
            nx.draw_networkx_nodes(self.g, pos, nodelist=ruta_destacada, node_color="red", node_size=600)
        
        plt.show()
    
    def procesar_solicitud(self, v):
            if v == 1:
                def accion():
                    self.ventana.geometry("600x448+240+240")
                    x=int(pe1.get())
                    y=int(pe2.get())
                    inicio = self.lisD[x - 1]
                    destino = self.lisD[y - 1]
                    ruta = self.ruta_mas_corta(inicio, destino)
                    ru = tk.Label(self.ventana, text=f"La ruta más eficiente es:\n" + "\n".join(ruta), font=("Arial", 10))
                    ru.grid(row=3, column=1)
                    self.mostrar(ruta_destacada=ruta)
                
                def salir():
                    self.ventana.destroy()
                    self.menuPrincipal()
                
                self.crear_nodos()     
                self.crear_conexiones()
                self.ventana.geometry("600x300+240+240")
                titulo=tk.Label(self.ventana, text="Te mostraremos la ruta mas eficiente", font=("Arial", 18))
                i=0
                for nombre, datos in self.info.items():
                        i += 1
                        op=tk.Label(self.ventana, text=f"{i}.{nombre}", font=("Arial", 14))
                        op.grid(row=i, column=0)
                p1=tk.Label(self.ventana, text="Desde que pais vienes?", font=("Arial", 14))
                p2=tk.Label(self.ventana, text="A que pais quires ir?", font=("Arial", 14))
                pe1=tk.Entry(self.ventana)
                pe2=tk.Entry(self.ventana)
                bm=tk.Button(self.ventana, text="Mostrar",command=accion, font=("Arial", 14))
                bs=tk.Button(self.ventana, text="Salir",command=salir, font=("Arial", 14))
                titulo.grid(row=0, column=0)
                p1.grid(row=i+1, column=0)
                p2.grid(row=i+2, column=0)
                pe1.grid(row=i+1, column=1)
                pe2.grid(row=i+2, column=1)
                bm.grid(row=i+3, column=1)
                bs.grid(row=i+3, column=0)
            elif v == 2:
                def quitar():
                    titulo1.destroy()
                    titulo2.destroy()
                    aer.destroy()
                    aere.destroy()
                    bc.destroy()
                    bg.destroy()
                    bb.destroy()
                    for label in self.ari_labels:
                        label.destroy()
                    self.ari_labels.clear()
                    
                def grafo():
                    self.mostrar()
                
                def busruta():
                    def graforu():
                        x=int(pe1.get())
                        y=int(pe2.get())
                        inicio = self.lisD[x - 1]
                        destino = self.lisD[y - 1]
                        ruta = self.ruta_mas_corta(inicio, destino)
                        ru = tk.Label(self.ventana, text=f"La ruta más eficiente es:\n" + "\n".join(ruta), font=("Arial", 10))
                        ru.grid(row=3, column=1)
                        self.mostrar(ruta_destacada=ruta)
                        
                    quitar()
                    self.ventana.geometry("600x300+240+240")
                    titulo.config(text="Te mostraremos la ruta mas eficiente")
                    p1.config(text="Desde que pais vienes?")
                    p2.config(text="A que pais quires ir?")
                    bm=tk.Button(self.ventana, text="Mostrar",command=graforu, font=("Arial", 14))
                    bm.grid(row=i+5, column=1)

                def accion():
                    x=int(pe1.get())
                    y=int(pe2.get())
                    z=int(aere.get())
                    self.g.add_edge(self.lisD[x-1], self.lisD[y-1], weight=1, airline=self.Aero[z-1])
                    messagebox.showinfo("","Conexion Creada")
                
                def salir():
                    self.ventana.destroy()
                    self.menuPrincipal()
                self.ari_labels = []
                self.crear_nodos()
                self.ventana.geometry("600x400+240+240")
                titulo=tk.Label(self.ventana, text="Crea tus conexiones", font=("Arial", 18))
                titulo1=tk.Label(self.ventana, text="Paises", font=("Arial", 15))
                titulo2=tk.Label(self.ventana, text="Aerolienas", font=("Arial", 15))
                i=1
                for nombre, datos in self.info.items():
                        i += 1
                        op=tk.Label(self.ventana, text=f"{i-1}.{nombre}", font=("Arial", 14))
                        op.grid(row=i, column=0)
                z=1
                for nombre in self.Aero:
                    z += 1 
                    ari=tk.Label(self.ventana, text=f"{z-1}.{nombre}", font=("Arial", 14))
                    ari.grid(row=z, column=1)
                    self.ari_labels.append(ari)
                p1=tk.Label(self.ventana, text="Cual es el pais de donde saldra la arista?", font=("Arial", 14))
                p2=tk.Label(self.ventana, text="A cual se conecta?", font=("Arial", 14))
                aer=tk.Label(self.ventana, text="Que Aerolinea es la que conecta?", font=("Arial", 14))
                pe1=tk.Entry(self.ventana)
                pe2=tk.Entry(self.ventana)
                aere=tk.Entry(self.ventana)
                bc=tk.Button(self.ventana, text="Conectar",command=accion, font=("Arial", 14))
                bg=tk.Button(self.ventana, text="Ver Grafo",command=grafo, font=("Arial", 14))
                bs=tk.Button(self.ventana, text="Salir",command=salir, font=("Arial", 14))
                bb=tk.Button(self.ventana, text="Buscar ruta mas corta",command=busruta, font=("Arial", 14))
                titulo.grid(row=0, column=0)
                titulo1.grid(row=1, column=0)
                titulo2.grid(row=1, column=1)
                p1.grid(row=i+1, column=0)
                p2.grid(row=i+2, column=0)
                aer.grid(row=i+3, column=0)
                pe1.grid(row=i+1, column=1)
                pe2.grid(row=i+2, column=1)
                aere.grid(row=i+3, column=1)
                bc.grid(row=i+4, column=1)
                bs.grid(row=i+5, column=0)
                bg.grid(row=i+4, column=0)
                bb.grid(row=i+5, column=1)

    def salir(self):
        self.ventana.destroy()
        g=impo()
        g.menuPrincipal()

    def acerca_de(self):
        messagebox.showinfo("Acerca de los Desarolladores", "Delucio Fuentes Ricardo Ismael \nSoberanes Flores Ricardo")

    def menuPrincipal(self):
        self.cargar_J()
        def acciones(x):
            titulo.destroy()
            intro.destroy()
            Op1.destroy()
            Op2.destroy()
            b1.destroy()
            b2.destroy()
            self.procesar_solicitud(x)
        
        self.ventana = tk.Tk()
        self.ventana.title("AeroPaletas")
        self.ventana.geometry("780x300+240+240")
        menu_principal=tk.Menu(self.ventana)
        
        menu_principal.add_cascade(label="Salir", command=self.salir)
        menu_principal.add_cascade(label="Acerca de los Alumnos", command=self.acerca_de)
        
        titulo=tk.Label(self.ventana, text="Bienvenido a Aeropaletas", font=("Arial", 18))
        intro=tk.Label(self.ventana, text="Que es lo primero que quieres hacer hoy?", font=("Arial", 14))
        Op1=tk.Label(self.ventana, text="Conexiones Automaticas", font=("Arial", 14))
        Op2=tk.Label(self.ventana, text="Conexiones Manuales", font=("Arial", 14))
        b1=tk.Button(self.ventana, text="Continuar",command=lambda:acciones(1), font=("Arial", 14))
        b2=tk.Button(self.ventana, text="Continuar",command=lambda:acciones(2), font=("Arial", 14))
        titulo.grid(row=0, column=2)
        intro.grid(row=1, column=2)
        Op1.grid(row=2, column=0)
        Op2.grid(row=2, column=3)
        b1.grid(row=3, column=0)
        b2.grid(row=3, column=3)
        self.ventana.config(menu=menu_principal)

        self.ventana.mainloop()


