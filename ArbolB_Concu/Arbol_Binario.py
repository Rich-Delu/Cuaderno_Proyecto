import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class Nodo:
  def __init__(self, cd, nom,dom):
    self.codigo= cd
    self.nombre=nom
    self.domicilio=dom
    self.izq= None
    self.der= None
  
  def __str1__(self):
    return f"{self.codigo} \n {self.nombre}"

  def __str2__(self):
    return f"{self.codigo} \n {self.nombre} \n {self.domicilio}"

class ABB1:
  def __init__(self):
    self.raiz= None

  def insertar(self, tx, txt):
    if self.raiz is None:
      self.raiz= Nodo(tx, txt)
    else:
      self._insertar_recursividad(self.raiz, tx, txt)

  def _insertar_recursividad(self, nodo, tx, txt):
    if tx < nodo.codigo:
      if nodo.izq is None:
        nodo.izq= Nodo(tx, txt)
      else:
        self._insertar_recursividad(nodo.izq, tx, txt)
    elif tx > nodo.codigo:
      if nodo.der is None:
        nodo.der= Nodo(tx, txt)
      else:
        self._insertar_recursividad(nodo.der, tx, txt)

  def vizualizar(self):
    self._vizualizar_recursividad(self.raiz)
    pos = nx.spring_layout(self.g)
    nx.draw(self.g, pos, with_labels=True, font_color='black', node_color='#A569BD', node_size=500,font_size=8, arrows=True)
    edge_labels = nx.get_edge_attributes(self.g, 'weight')
    nx.draw_networkx_edge_labels(self.g, pos, edge_labels=edge_labels)
    plt.show()

  def _vizualizar_recursividad(self, nodo):
    etiqueta=f"{nodo.__str__()}"
    if nodo.izq is not None:
      self.g.add_edge(str(etiqueta), str(nodo.izq))
      self._vizualizar_recursividad(nodo.izq)

    if nodo.der is not None:
      self.g.add_edge(str(etiqueta), str(nodo.der))
      self._vizualizar_recursividad(nodo.der)
  
  def ingresar(self):
      self.insertar("JA","JORGE AVILA")
      self.insertar("CM","CARLA MORALES")
      self.insertar("BT","BERTHA TORRES")
      self.insertar("AP","ANDRES PEREZ")
      self.insertar("RM","RAUL MENA")
      self.insertar("ZD","ZAIRA DELGADO")
      
  def menuPrincipal1(self):
        self.ingresar()
        def acciones(x):
            if x==1:
              self.info.delete("1.0", tk.END)
              self.inorden()
            elif x==2:
              self.info.delete("1.0", tk.END)
              self.preorden()
            elif x ==3:
              self.info.delete("1.0", tk.END)
              self.postorden()
            elif x==4:
              self.vizualizar()
        
        def salir():
            g=impo()
            messagebox.showinfo("","Adios")
            g.menuPrincipal()

        self.ventana = tk.Tk()
        self.ventana.title("Arbol Binario")
        self.ventana.geometry("700x350+240+240")
        menu_principal=tk.Menu(self.ventana)

        titulo=tk.Label(self.ventana, text="Arbol Binario", font=("Arial", 18))
        b1=tk.Button(self.ventana, text="Vizualizar",command=lambda:acciones(1), font=("Arial", 14))
        bs=tk.Button(self.ventana, text="Salir", command=salir(), font=("Arial", 14))
        titulo.grid(row=0, column=0)
        b1.grid(row=1, column=0)
        bs.grid(row=2, column=0)
        self.ventana.config(menu=menu_principal)

        self.ventana.mainloop()

class ABB2:
  def __init__(self):
    self.g = nx.DiGraph()
    self.raiz= None

  def insertar(self, tx, txt,text):
    if self.raiz is None:
      self.raiz= Nodo(tx, txt, text)
    else:
      self._insertar_recursividad(self.raiz, tx, txt, text)

  def _insertar_recursividad(self, nodo, tx, txt, text):
    if tx < nodo.codigo:
      if nodo.izq is None:
        nodo.izq= Nodo(tx, txt, text)
      else:
        self._insertar_recursividad(nodo.izq, tx, txt, text)
    elif tx > nodo.codigo:
      if nodo.der is None:
        nodo.der= Nodo(tx, txt, text)
      else:
        self._insertar_recursividad(nodo.der, tx, txt, text)

  def vizualizar(self):
    self._vizualizar_recursividad(self.raiz)
    pos = nx.spring_layout(self.g)
    nx.draw(self.g, pos, with_labels=True, font_color='black', node_color='#A569BD', node_size=500,font_size=8, arrows=True)
    edge_labels = nx.get_edge_attributes(self.g, 'weight')
    nx.draw_networkx_edge_labels(self.g, pos, edge_labels=edge_labels)
    plt.show()

  def _vizualizar_recursividad(self, nodo):
    etiqueta=f"{nodo.__str__()}"
    if nodo.izq is not None:
      self.g.add_edge(str(etiqueta), str(nodo.izq))
      self._vizualizar_recursividad(nodo.izq)

    if nodo.der is not None:
      self.g.add_edge(str(etiqueta), str(nodo.der))
      self._vizualizar_recursividad(nodo.der)

  def inorden(self):
      self._inorden_re(self.raiz)
      print()

  def _inorden_re(self, nodo):
    if nodo is not None:
      self._inorden_re(nodo.izq)
      self.info.insert(tk.END, f"{nodo.codigo} - {nodo.nombre} - {nodo.domicilio} \n")
      print()
      self._inorden_re(nodo.der)

  def preorden(self):
    self._preorden_re(self.raiz)
    print()

  def _preorden_re(self, nodo):
    if nodo is not None:
      self.info.insert(tk.END, f"{nodo.codigo} - {nodo.nombre} - {nodo.domicilio} \n")
      print()
      self._preorden_re(nodo.izq)
      self._preorden_re(nodo.der)

  def postorden(self):
    self._postorden_re(self.raiz)
    print()

  def _postorden_re(self, nodo):
    if nodo is not None:
      self._postorden_re(nodo.izq)
      self._postorden_re(nodo.der)
      self.info.insert(tk.END, f"{nodo.codigo} - {nodo.nombre} - {nodo.domicilio} \n")
      print()

  def ingresar(self):
      self.insertar("LP","Luis Perez", "Av.Reforma 100")
      self.insertar("AT","Ana Torres","Calle Norte 456")
      self.insertar("JG","Juan Gomez", "Insurgente 789")
      self.insertar("KM","Karla Morales", "Copilco 34")
      self.insertar("BTT","Bertha Torre", "Venezuela 8")
      self.insertar("AP","Adrian Perez", "Centro 24")
      
  def menuPrincipal(self):
        self.ingresar()
        def acciones(x):
            if x==1:
              self.info.delete("1.0", tk.END)
              self.inorden()
            elif x==2:
              self.info.delete("1.0", tk.END)
              self.preorden()
            elif x ==3:
              self.info.delete("1.0", tk.END)
              self.postorden()
            elif x==4:
              self.vizualizar()

        def salir():
            g=impo()
            messagebox.showinfo("","Adios")
            g.menuPrincipal()
            
        self.ventana = tk.Tk()
        self.ventana.title("Arbol Binario")
        self.ventana.geometry("700x350+240+240")
        menu_principal=tk.Menu(self.ventana)

        titulo=tk.Label(self.ventana, text="Opciones de Busqueda", font=("Arial", 18))
        Op1=tk.Label(self.ventana, text="Inorden", font=("Arial", 14))
        Op2=tk.Label(self.ventana, text="Postorden", font=("Arial", 14))
        Op3=tk.Label(self.ventana, text="Preorden", font=("Arial", 14))
        b1=tk.Button(self.ventana, text="Continuar",command=lambda:acciones(1), font=("Arial", 14))
        b2=tk.Button(self.ventana, text="Continuar",command=lambda:acciones(2), font=("Arial", 14))
        b3=tk.Button(self.ventana, text="Continuar",command=lambda:acciones(3), font=("Arial", 14))
        ar=tk.Button(self.ventana, text="Visualizar Arbol",command=lambda:acciones(4), font=("Arial", 14))
        bs=tk.Button(self.ventana, text="Salir",command=salir, font=("Arial", 14))
        self.info=tk.Text(self.ventana, width=40, height=10)
        self.info.grid(row=2,column=3)
        titulo.grid(row=0, column=0)
        Op1.grid(row=1, column=0)
        Op2.grid(row=2, column=0)
        Op3.grid(row=3, column=0)
        b1.grid(row=1, column=1)
        b2.grid(row=2, column=1)
        b3.grid(row=3, column=1)
        ar.grid(row=4, column=0)
        bs.grid(row=5, column=1)
        self.ventana.config(menu=menu_principal)

        self.ventana.mainloop()

if __name__ == '__main:__':
    a1=ABB1()
    a1.menuPrincipal1()