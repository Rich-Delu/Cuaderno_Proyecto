import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class Aeropuertos:
    def __init__(self):
        self.g = nx.DiGraph()
        self.dicDestinos = {
            "Op1": {"Nombre": "Suiza", "Costo de Hospedaje": "18000-23000$", "Recomendable": "80%"},
            "Op2": {"Nombre": "Italia", "Costo de Hospedaje": "14000-22000$", "Recomendable": "60%"},
            "Op3": {"Nombre": "Francia", "Costo de Hospedaje": "29000-30000$", "Recomendable": "70%"},
            "Op4": {"Nombre": "Alemania", "Costo de Hospedaje": "14000-18000$", "Recomendable": "70%"},
            "Sal": {"Nombre": "CDMX", "Costo de Hospedaje": "15000-23000$", "Recomendable": "80%"}
        }
        self.dicAerolineas = {
            "Op1": {"Nombre": "Magnicharters", "Costo": "18000-23000$", "Seguridad": "Segura", "Peso": 7},
            "Op2": {"Nombre": "AeroMexico", "Costo": "14000-22000$", "Seguridad": "Muy Seguro", "Peso": 6},
            "Op3": {"Nombre": "Volaris", "Costo": "29000-30000$", "Seguridad": "Muy Segura", "Peso": 8},
            "Op4": {"Nombre": "Iberia", "Costo": "14000-18000$", "Seguridad": "Muy Segura", "Peso": 4},
        }

    def crear_nodos(self):
        self.lisAero=[]
        self.lisDesti=[]
        for i in self.dicDestinos:
            nodosDes = f"Nombre: {self.dicDestinos[i]['Nombre']}\nCosto de Hospedaje: {self.dicDestinos[i]['Costo de Hospedaje']}\nRecomendable: {self.dicDestinos[i]['Recomendable']}"
            self.lisDesti.append(nodosDes)
        self.g.add_nodes_from(self.lisDesti)
        for i in self.dicAerolineas:
            nodoAer = f"Nombre: {self.dicAerolineas[i]['Nombre']}\nCosto: {self.dicAerolineas[i]['Costo']}\nSeguridad: {self.dicAerolineas[i]['Seguridad']}"
            self.lisAero.append(nodoAer)
        self.g.add_nodes_from(self.lisAero)

    def crear_conexiones(self):
        pesos = [self.dicAerolineas[i]['Peso'] for i in self.dicAerolineas]
        
        for i in range(len(self.lisAero)):
            self.g.add_edge(self.lisDesti[4], self.lisAero[i])

        for i, peso in enumerate(pesos):
            if i < len(self.lisAero):  
                self.g.add_edge(self.lisAero[i], self.lisDesti[i], weight=peso)

        self.g.add_edge(self.lisAero[3], self.lisDesti[0], weight=pesos[3])

    def bfs(self, inicio):
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

    def mostrar(self):
        self.crear_nodos()
        self.crear_conexiones()
        pos = nx.spring_layout(self.g)
        nx.draw(self.g, pos, with_labels=True, font_color='black', node_color='#A569BD', node_size=500,font_size=8, arrows=True)
        edge_labels = nx.get_edge_attributes(self.g, 'weight')
        nx.draw_networkx_edge_labels(self.g, pos, edge_labels=edge_labels)
        plt.show()
