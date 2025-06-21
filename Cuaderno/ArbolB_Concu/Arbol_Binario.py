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
  def __init__(self, cd, nom,dom, p1, p2, p3):
    self.codigo= cd
    self.nombre=nom
    self.domicilio=dom
    self.p1= p1
    self.p2= p2
    self.p3= p3
    if self.p1 is None:
      self.prom=None
    else:
      self.prom=(self.p1+self.p2+self.p3)/3
    self.izq= None
    self.der= None
    
  def __str__(self):
    if self.domicilio is None:
        return f"{self.codigo} \n {self.nombre}"
    elif self.prom is not None:
        return f"{self.codigo} \n {self.nombre} \n {self.prom:.2f}"
    else:
        return f"{self.codigo} \n {self.nombre} \n {self.domicilio}"

class ABB1:
    def __init__(self):
      self.g = nx.DiGraph()
      self.raiz= None
      self.xd= None
      self.x1= None
      self.x2 = None
      self.x3 = None

    def insertar(self, tx, txt):
      if self.raiz is None:
        self.raiz= Nodo(tx, txt, self.xd, self.x1, self.x2, self.x3)
      else:
        self._insertar_recursividad(self.raiz, tx, txt)

    def _insertar_recursividad(self, nodo, tx, txt):
      if tx < nodo.codigo:
        if nodo.izq is None:
          nodo.izq= Nodo(tx, txt, self.xd, self.x1, self.x2, self.x3)
        else:
          self._insertar_recursividad(nodo.izq, tx, txt)
      elif tx > nodo.codigo:
        if nodo.der is None:
          nodo.der= Nodo(tx, txt, self.xd, self.x1, self.x2, self.x3)
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
        
    def salir(self):
        g=impo()
        self.ventana.destroy()
        messagebox.showinfo("","Adios")
        g.menuPrincipal()
      
    def menuPrincipal(self):
      self.ingresar()
      self.ventana = tk.Tk()
      self.ventana.title("Arbol Binario")
      self.ventana.geometry("200x200+240+240")

      titulo=tk.Label(self.ventana, text="Arbol Binario", font=("Arial", 18))
      b1=tk.Button(self.ventana, text="Vizualizar",command=self.vizualizar, font=("Arial", 14))
      bs=tk.Button(self.ventana, text="Salir", command=self.salir, font=("Arial", 14))
      titulo.grid(row=0, column=0)
      b1.grid(row=1, column=0)
      bs.grid(row=2, column=0)
      
      self.ventana.mainloop()

class ABB2:
  def __init__(self):
    self.g = nx.DiGraph()
    self.raiz= None
    self.x1= None
    self.x2 = None
    self.x3 = None

  def insertar(self, tx, txt,text):
    if self.raiz is None:
      self.raiz= Nodo(tx, txt, text, self.x1, self.x2, self.x3)
    else:
      self._insertar_recursividad(self.raiz, tx, txt, text)

  def _insertar_recursividad(self, nodo, tx, txt, text,):
    if tx < nodo.codigo:
      if nodo.izq is None:
        nodo.izq= Nodo(tx, txt, text, self.x1, self.x2, self.x3)
      else:
        self._insertar_recursividad(nodo.izq, tx, txt, text)
    elif tx > nodo.codigo:
      if nodo.der is None:
        nodo.der= Nodo(tx, txt, text, self.x1, self.x2, self.x3)
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
          self.ventana.destroy( )
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

class ABB3:
  def __init__(self):
    self.g = nx.DiGraph()
    self.raiz= None
    self.xd = 0

  def insertar(self, bol, nom, p1, p2, p3):
    if self.raiz is None:
      self.raiz= Nodo(bol, nom, self.xd, p1, p2, p3)
    else:
      self._insertar_recursividad(self.raiz, bol, nom, p1, p2, p3)

  def _insertar_recursividad(self, nodo, bol, nom, p1, p2, p3):
    if bol < nodo.codigo:
      if nodo.izq is None:
        nodo.izq= Nodo(bol, nom, self.xd, p1, p2, p3)
      else:
        self._insertar_recursividad(nodo.izq, bol, nom, p1, p2, p3)
    elif bol > nodo.codigo:
      if nodo.der is None:
        nodo.der= Nodo(bol, nom, self.xd, p1, p2, p3)
      else:
        self._insertar_recursividad(nodo.der, bol, nom, p1, p2, p3)

  def leer(self):
    def agregar():
      x1=int(bole.get())
      x2=nome.get()
      x3=int(p1e.get())
      x4=int(p2e.get())
      x5=int(p3e.get())
      self.insertar(x1, x2, x3, x4, x5)
      messagebox.showinfo("",f"Alumno {x2} Agregado")
    
    def salir():
      self.ventana.destroy()
      self.menu()
      
    bol=tk.Label(self.ventana, text="Dame la Boleta del Alumno:", font=("Arial", 14))
    nom=tk.Label(self.ventana, text="Dame el Nombre del Alumno:", font=("Arial", 14))
    p1=tk.Label(self.ventana, text="Dame la Calificacion del Parcial 1 del Alumno:", font=("Arial", 14))
    p2=tk.Label(self.ventana, text="Dame la Calificacion del Parcial 2 del Alumno:", font=("Arial", 14))
    p3=tk.Label(self.ventana, text="Dame la Calificacion del Parcial 3 del Alumno:", font=("Arial", 14))
    bole=tk.Entry(self.ventana)
    nome=tk.Entry(self.ventana)
    p1e=tk.Entry(self.ventana)
    p2e=tk.Entry(self.ventana)
    p3e=tk.Entry(self.ventana)
    ba=tk.Button(self.ventana, text="Agregar", command=agregar)
    bs=tk.Button(self.ventana, text="Salir", command=salir)
    bol.grid(row=0, column=0)
    nom.grid(row=1, column=0)
    p1.grid(row=2, column=0)
    p2.grid(row=3, column=0)
    p3.grid(row=4, column=0)
    bole.grid(row=0, column=1)
    nome.grid(row=1, column=1)
    p1e.grid(row=2, column=1)
    p2e.grid(row=3, column=1)
    p3e.grid(row=4, column=1)
    ba.grid(row=6, column=1)
    bs.grid(row=6, column=0)

  def eliminar(self):
    def el():
      x1=int(bole.get())
      self.raiz = self._eliminar_recursivamente(self.raiz, x1)
      messagebox.showinfo("",f"Alumno Eliminado")
    
    def salir():
      self.ventana.destroy()
      self.menu()
      
    bol=tk.Label(self.ventana, text="Dame la Boleta del Alumno a Eliminar:", font=("Arial", 14))
    bole=tk.Entry(self.ventana)
    be=tk.Button(self.ventana, text="Eliminar", command=el)
    bs=tk.Button(self.ventana, text="Salir", command=salir)
    bol.grid(row=0, column=0)
    bole.grid(row=0, column=1)
    be.grid(row=2, column=1)
    bs.grid(row=2, column=0)

  def _eliminar_recursivamente(self, nodo, bol):
      if nodo is None:
          return None

      if bol < nodo.codigo:
          nodo.izq = self._eliminar_recursivamente(nodo.izq, bol)
      elif bol > nodo.codigo:
          nodo.der = self._eliminar_recursivamente(nodo.der, bol)
      else:
          if nodo.izq is None and nodo.der is None:
              return None
          elif nodo.izq is None:
              return nodo.der
          elif nodo.der is None:
              return nodo.izq
          else:
              sucesor = self._encontrar_minimo(nodo.der)
              nodo.codigo = sucesor.codigo
              nodo.nombre = sucesor.nombre
              nodo.p1 = sucesor.p1
              nodo.p2 = sucesor.p2
              nodo.p3 = sucesor.p3
              nodo.der = self._eliminar_recursivamente(nodo.der, sucesor.codigo)
      return nodo

  def _encontrar_minimo(self, nodo):
      while nodo.izq is not None:
          nodo = nodo.izq
      return nodo

  def profundidad(self):
      return self._profundidad_recursiva(self.raiz)

  def _profundidad_recursiva(self, nodo):
      if nodo is None:
        return 0
      izq_profundidad = self._profundidad_recursiva(nodo.izq)
      der_profundidad = self._profundidad_recursiva(nodo.der)
      return max(izq_profundidad, der_profundidad) + 1

  def buscar(self):
    def accion():
      x1=int(bole.get())
      nodo = self._buscar_recursivo(self.raiz, x1)
      if nodo:
        messagebox.showinfo("",f"Alumno encontrado: {nodo}")
      else:
        messagebox.showinfo("",f"Alumno no encontrado")
    
    def salir():
      self.ventana.destroy()
      self.menu()
      
    bol=tk.Label(self.ventana, text="Dame la Boleta del Alumno a Buscar:", font=("Arial", 14))
    bole=tk.Entry(self.ventana)
    bb=tk.Button(self.ventana, text="Buscar", command=accion)
    bs=tk.Button(self.ventana, text="Salir", command=salir)
    bol.grid(row=0, column=0)
    bole.grid(row=0, column=1)
    bb.grid(row=2, column=1)
    bs.grid(row=2, column=0)

  def _buscar_recursivo(self, nodo, bol):
    if nodo is None:
        return None
    if bol == nodo.codigo:
        return nodo
    elif bol < nodo.codigo:
        return self._buscar_recursivo(nodo.izq, bol)
    else:
        return self._buscar_recursivo(nodo.der, bol)
      
  def vizualizar(self):
    if self.raiz is None:
        print("El árbol está vacío. No hay nada que visualizar.")
        return
    self.g.clear() 
    
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

  def pros_busque(self):
      def accion():
        x=int(Ene.get())
        if x==1:
          info.delete("1.0", tk.END)
          self.inorden(x, info)
        elif x==2:
          info.delete("1.0", tk.END)
          self.preorden(x, info)
        elif x ==3:
          info.delete("1.0", tk.END)
          self.postorden(x, info)
        else:
          messagebox.showinfo("","Opcion Invalida")
      
      def salir():
        self.ventana.destroy()
        self.menu()
      
      self.ventana.geometry("500x350+240+240")
      
      frame_contenedor_izq = tk.Frame(self.ventana, bg="white", padx=10, pady=10)
      frame_contenedor_izq.grid(row=0, column=0, columnspan=2, sticky="nsew")

      titulo = tk.Label(frame_contenedor_izq, text="Menu de Opciones", font=("Arial", 18))
      titulo.grid(row=0, column=0, columnspan=2, pady=10)

      In = tk.Label(frame_contenedor_izq, text="1. Inorden", font=("Arial", 14))
      In.grid(row=1, column=0, padx=10, pady=5, sticky="w")

      Pre = tk.Label(frame_contenedor_izq, text="2. Preorden", font=("Arial", 14))
      Pre.grid(row=2, column=0, padx=10, pady=5, sticky="w")

      Post = tk.Label(frame_contenedor_izq, text="3. Postorden", font=("Arial", 14))
      Post.grid(row=3, column=0, padx=10, pady=5, sticky="w")

      info = tk.Text(frame_contenedor_izq, width=40, height=10)
      info.grid(row=1, column=1, rowspan=3, padx=10, pady=5)

      Ene = tk.Entry(frame_contenedor_izq)
      Ene.grid(row=4, column=0, padx=10, pady=10, sticky="we")

      bb = tk.Button(frame_contenedor_izq, text="Continuar", command=accion, font=("Arial", 14))
      bb.grid(row=5, column=0, padx=10, pady=10)
      
      bs = tk.Button(frame_contenedor_izq, text="Salir", command=salir, font=("Arial", 14))
      bs.grid(row=5, column=1, padx=10, pady=10)

      frame_contenedor_izq.columnconfigure(1, weight=1)
      frame_contenedor_izq.rowconfigure(1, weight=1)
      frame_contenedor_izq.rowconfigure(2, weight=1)
      frame_contenedor_izq.rowconfigure(3, weight=1)

  def inorden(self, nodo, info):
      self._inorden_re(self.raiz, info)
      print()

  def _inorden_re(self, nodo, info):
    etiqueta=f"{nodo.__str__()}"
    if nodo is not None:
      self._inorden_re(nodo.izq, info)
      info.insert(tk.END, f"{etiqueta}\n")
      self._inorden_re(nodo.der, info)

  def preorden(self, nodo, info):
    self._preorden_re(self.raiz, info)
    print()

  def _preorden_re(self, nodo, info):
    etiqueta=f"{nodo.__str__()}"
    if nodo is not None:
      info.insert(tk.END, f"{etiqueta}\n")
      self._preorden_re(nodo.izq, info)
      self._preorden_re(nodo.der, info)

  def postorden(self,nodo, info):
    self._postorden_re(self.raiz, info)
    print()

  def _postorden_re(self, nodo, info):
    etiqueta=f"{nodo.__str__()}"
    if nodo is not None:
      self._postorden_re(nodo.izq, info)
      self._postorden_re(nodo.der, info)
      info.insert(tk.END, f"{etiqueta}\n")
  
  def ingresar(self):
      self.insertar(20201234,"Ana Lopez", 10, 7, 5)
      self.insertar(20201111,"Carlos Perez", 9, 6, 8)
      self.insertar(20204567,"Luis Hernandez", 7, 7, 8)
      self.insertar(20203456,"Marta Rivera", 8, 7, 9)
      self.insertar(20207890,"Sofia Torres", 6, 7, 6)
             
  def menu(self):
      self.ingresar()
      def destroy():
          Op1.destroy()
          Op2.destroy()
          Op3.destroy()
          Op4.destroy()
          Op5.destroy()
          Op6.destroy()
          Op7.destroy()
          En.destroy()
          b1.destroy()
          
      def acciones():
          g=impo()
          opcion=int(En.get())
          if opcion == 1:
            destroy()
            self.leer()
          elif opcion == 2:
            destroy()
            self.eliminar()
          elif opcion == 3:
            messagebox.showinfo("",f"La profundidad del arbol es:{self.profundidad()}")
          elif opcion == 4:
            destroy()
            self.buscar()
          elif opcion == 5:
            self.vizualizar()
          elif opcion == 6:
            destroy()
            self.pros_busque()
          elif opcion == 7:
            self.ventana.destroy( )
            messagebox.showinfo("","Adios")
            g.menuPrincipal()
          else:
            messagebox.showinfo("","Opcion Invalida")
            
      self.ventana = tk.Tk()
      self.ventana.title("Arbol Binario")
      self.ventana.geometry("480x350+240+240")

      titulo=tk.Label(self.ventana, text="Menu de Opciones", font=("Arial", 18))
      Op1=tk.Label(self.ventana, text="1.Insertar Alumno", font=("Arial", 14))
      Op2=tk.Label(self.ventana, text="2.Eliminar Alumno", font=("Arial", 14))
      Op3=tk.Label(self.ventana, text="3.Mostrar Profundidad del Arbol", font=("Arial", 14))
      Op4=tk.Label(self.ventana, text="4.Buscar Alumno", font=("Arial", 14))
      Op5=tk.Label(self.ventana, text="5.Mostrar Arbol", font=("Arial", 14))
      Op6=tk.Label(self.ventana, text="6.Ver orden de Busqueda", font=("Arial", 14))
      Op7=tk.Label(self.ventana, text="7.Salir", font=("Arial", 14))
      En=tk.Entry(self.ventana)
      b1=tk.Button(self.ventana, text="Continuar",command=acciones, font=("Arial", 14))
      titulo.grid(row=0, column=0)
      Op1.grid(row=1, column=0)
      Op2.grid(row=2, column=0)
      Op3.grid(row=3, column=0)
      Op4.grid(row=4, column=0)
      Op5.grid(row=5, column=0)
      Op6.grid(row=6, column=0)
      Op7.grid(row=7, column=0)
      En.grid(row=8, column=0)
      b1.grid(row=9, column=0)

      self.ventana.mainloop()