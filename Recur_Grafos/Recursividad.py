import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

def sumaNaturales(n):
    if n == 1:
        return 1
    else:
        return n +sumaNaturales(n-1)

def menu1_R():
    g=impo()
    def accion():
        x=int(ece.get())
        messagebox.showinfo("",f"la suma de los primero {x} numeros naturales es: {sumaNaturales(x)}")
    
    def salir():
        ventana.destroy()
        messagebox.showinfo("","Adios")
        g.menuPrincipal()
    
    ventana = tk.Tk()
    ventana.title("Suma de Numeros Naturales")
    ventana.geometry("600x400+240+240")
    ec=tk.Label(ventana, text="Dame el valor de n", justify="left", font=("Arial", 14))
    ece=tk.Entry(ventana)
    ece.grid(padx=0,pady=5, row=0, column=1)
    b1=tk.Button(ventana, text="Sumar", font=("Arial",14), command=accion)
    bS=tk.Button(ventana, text="Salir", font=("Arial",14), command=salir)
    ec.grid(pady=5, row=0, column=0)
    b1.grid(padx=0,pady=5, row=1, column=0)
    bS.grid(padx=0,pady=5, row=1, column=1)

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None

    def insertarInicio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.inicio:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
        self.inicio = nuevo_nodo

    def insertarFinal(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.inicio:
            self.inicio = nuevo_nodo
            return
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual

    def eliminar(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.inicio:
                    self.inicio = actual.siguiente
                return
            actual = actual.siguiente

    def mostrarAdelanteHaciaAtras(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def mostrarAtrasHaciaAdelante(self):
        actual = self.inicio
        if not actual:
            return
        while actual.siguiente:
            actual = actual.siguiente
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")

class Resistencias(ListaDobleEnlazada):
    def __init__(self):
        super().__init__()

    def sumar_en_serie(self):
        actual = self.inicio
        suma = 0
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma

    def sumar_en_paralelo(self):
        actual = self.inicio
        suma = 0
        while actual:
            suma += 1 / actual.dato
            actual = actual.siguiente
        return 1 / suma

    def solicitar_resistencias(self, ventana, i, x, res):
        def suma():
            resistencia=int(re.get())
            self.insertarInicio(resistencia)
            messagebox.showinfo("",f"Resistencia con valor: {resistencia} agregada")
        
        def ver_resul():
            suma = self.sumar_en_serie() if i == 1 else self.sumar_en_paralelo()
            messagebox.showinfo("",f"La suma de las resistencias es: {suma:.2f}")
        
        def regresar():
            def quitar():
                re.destroy()
                r.destroy()
                bi.destroy()
                br.destroy()
            if i in (1,2):
                ventana.destroy()
                menu2_R()
            elif i==3:
                suma = self.sumar_en_serie() if x == 1 else self.sumar_en_paralelo()
                self.insertarInicio(suma)
                procesar_combinado(res, ventana,i)
                quitar()
        
        if i in (1,2):   
            r=tk.Label(ventana, text="Agrega el valor de las resistencia una por una", justify="left", font=("Arial", 14))
            re=tk.Entry(ventana)
            re.grid(padx=0,pady=5, row=0, column=1)
            bi=tk.Button(ventana, text="Agregar", font=("Arial",14), command=suma)
            bs=tk.Button(ventana, text="Ver Suma", font=("Arial",14), command=ver_resul)
            br=tk.Button(ventana, text="Regresar", font=("Arial",14), command=regresar)
            r.grid(pady=5, row=0, column=0)
            bs.grid(padx=0,pady=5, row=1, column=0)
            bi.grid(padx=0,pady=5, row=1, column=1)
            br.grid(padx=0,pady=5, row=2, column=0)
        elif i==3:
            r=tk.Label(ventana, text="Agrega el valor de las resistencia una por una", justify="left", font=("Arial", 14))
            re=tk.Entry(ventana)
            re.grid(padx=0,pady=5, row=0, column=1)
            bi=tk.Button(ventana, text="Agregar", font=("Arial",14), command=suma)
            br=tk.Button(ventana, text="Regresar", font=("Arial",14), command=regresar)
            r.grid(pady=5, row=0, column=0)
            bi.grid(padx=0,pady=5, row=1, column=1)
            br.grid(padx=0,pady=5, row=1, column=0)

def procesar_opcion(i, ventana):
    g=impo()
    res = Resistencias()
    if i in (1, 2):
        x=0
        res.solicitar_resistencias(ventana, i, x, res)
    elif i == 3:
        procesar_combinado(res, ventana,i)
    elif i == 4:
        ventana.destroy()
        messagebox.showinfo("","Adios")
        g.menuPrincipal()

def procesar_combinado(res, ventana, i):
    g=impo()
    def opc():
        def quitar():
            te.destroy()
            ba.destroy()
            bs.destroy()
            tipo.destroy()
            
        x=int(te.get())
        quitar()
        res.solicitar_resistencias(ventana, i, x, res)
    
    def ver_suma():
        if res.inicio is not None:
            messagebox.showinfo("",f"La suma de los nodos es: {res.inicio.dato:.2f}")
            res.mostrarAdelanteHaciaAtras()
        else:
            messagebox.showinfo("",f"No hay nodos para sumar")
    
    def salir():
        ventana.destroy()
        messagebox.showinfo("","Adios")
        g.menuPrincipal()
        
    tipo=tk.Label(ventana, text="1. En serie\n2. En paralelo\nSelecciona el tipo de nodo: ", justify="left", font=("Arial", 14))
    te=tk.Entry(ventana)
    tipo.grid(row=0,column=0)
    te.grid(row=1, column=0)
    ba=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=opc)
    bs=tk.Button(ventana, text="Ver suma", font=("Arial",14), command=ver_suma)
    bsalir=tk.Button(ventana, text="Ver suma", font=("Arial",14), command=salir)
    ba.grid(row=2, column=0)
    bs.grid(row=2, column=1)  
    bsalir.grid(row=3, column=0) 

def menu2_R():
    def ver_var():
        i=int(exe.get())
        procesar_opcion(i, ventana)
        tit.destroy()
        opc1.destroy()
        opc2.destroy()
        opc3.destroy()
        opc4.destroy() 
        exe.destroy()
        b1.destroy()
        
    ventana = tk.Tk()
    ventana.title("Suma de Resistencias en 1 o mas nodos")
    ventana.geometry("600x400+240+240")
    tit=tk.Label(ventana, text="Menu de Opciones", justify="left", font=("Arial", 14))
    opc1=tk.Label(ventana, text="1. Suma en Serie", justify="left", font=("Arial", 14))
    opc2=tk.Label(ventana, text="2. Suma en Paralelo", justify="left", font=("Arial", 14))
    opc3=tk.Label(ventana, text="3. Combinado", justify="left", font=("Arial", 14))
    opc4=tk.Label(ventana, text="4. Salir", justify="left", font=("Arial", 14))
    exe=tk.Entry(ventana)
    exe.grid(padx=0,pady=5, row=5, column=0)
    b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
    tit.grid(pady=5, row=0, column=0)
    opc1.grid(pady=5, row=1, column=0)
    opc2.grid(pady=5, row=2, column=0)
    opc3.grid(pady=5, row=3, column=0)
    opc4.grid(pady=5, row=4, column=0)
    b1.grid(padx=0,pady=5, row=6, column=0)