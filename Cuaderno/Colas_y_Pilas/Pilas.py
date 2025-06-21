import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class Pila1:
    def __init__(self):
        self._pila=[]

    def ver(self, ventana):
        def salir():
            ventana.destroy()
            self.menu()
        
        elem=tk.Label(ventana, text=f"Los Elementos de la Pila son:{self._pila}",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=2, column=1)

    def insertar(self, ventana):
        def ejecutar_accion():
            x=int(el.get())
            self._pila.append(x)
            messagebox.showinfo("",f"Agregado {x} a la Pila.")
        
        def salir():
            ventana.destroy()
            self.menu ()
            
        elem=tk.Label(ventana, text="Agrega el elemento deseado a la Pila:",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        el=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        el.grid(padx=5,pady=5, row=0, column=1)

    def extraer(self):
        if not self.estado():
            self._pila.pop()
            messagebox.showinfo("",f"Ultimo Elemento Eliminado de la Pila.")
        else:
            messagebox.showinfo("",f"No hay Elementos en la Pila")

    def consultar(self):
        if not self.estado():
            return self._pila[-1]
        return None

    def tamanio(self, ventana):
        def salir():
            ventana.destroy()
            self.menu ()
        
        x=len(self._pila)
        elem=tk.Label(ventana, text=f"El tamaño de la Pila es:{x}",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=2, column=1)

    def estado(self):
        return len(self._pila) == 0

    def menu(self):
        g=impo()
        def ver_var():
            def quitar():
                titulo.destroy()
                op1.destroy()
                op2.destroy()
                op3.destroy()
                op4.destroy()
                op5.destroy()  
                opc.destroy()
                b1.destroy()
            i=int(opc.get())
            if i == 1:
                quitar()
                self.insertar(ventana)
            elif i == 2:
                self.extraer()
            elif i == 3:
                quitar()
                self.tamanio(ventana)
            elif i == 4:
                quitar()
                self.ver(ventana)
            elif i == 5:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Pilas")
        ventana.geometry("600x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1.Insertar un elemento", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Extraer un elemento", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Consultar tamaño de la pila", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Vizualizar elementos en la Pila", justify="left", font=("Arial", 14))
        op5=tk.Label(ventana, text="5.Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=6, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=0, column=0)
        op1.grid(padx=0, pady=5, row=1, column=0)
        op2.grid(padx=0,pady=5, row=2, column=0)
        op3.grid(padx=0,pady=5, row=3, column=0)
        op4.grid(padx=0,pady=5, row=4, column=0)
        op5.grid(padx=0,pady=5,row=5, column=0)
        b1.grid(padx=0,pady=5, row=7, column=0)

class Pila2:
    def __init__(self):
        self._pila=[]

    def ver(self):
        print("Valores en la pila", self._pila)

    def insertar(self, valor):
        self._pila.append(valor)

    def extraer(self):
        if not self.estado():
            return self._pila.pop()
        return None

    def consultar(self):
        if not self.estado():
            return self._pila[-1]
        return None

    def tamanio(self):
        return len(self._pila)

    def estado(self):
        return len(self._pila) == 0

def parentesisBalanceados(x):
    pila = Pila2()
    for caracter in x:
        if caracter in "(":
            pila.insertar(caracter)
        elif caracter in ")":
            if pila.estado():
                return False
            par_apertura = pila.extraer()
            if par_apertura == "(" and caracter != ")":
                return False
    return pila.estado()

def menu1():
    g=impo()
    def accion():
        x=ece.get()
        if parentesisBalanceados(x):
            messagebox.showinfo("","La ecuacion está balanceada")
        else:
            messagebox.showinfo("","La ecuacion no está balanceada")
    
    def salir():
        ventana.destroy()
        messagebox.showinfo("","Adios")
        g.menuPrincipal()
    
    ventana = tk.Tk()
    ventana.title("Verificar Parentesis Balanceados")
    ventana.geometry("600x400+240+240")
    ec=tk.Label(ventana, text="Ingresa la Ecuacion Deseada", justify="left", font=("Arial", 14))
    ece=tk.Entry(ventana)
    ece.grid(padx=0,pady=5, row=0, column=1)
    b1=tk.Button(ventana, text="Verificar", font=("Arial",14), command=accion)
    bS=tk.Button(ventana, text="Salir", font=("Arial",14), command=salir)
    ec.grid(pady=5, row=0, column=0)
    b1.grid(padx=0,pady=5, row=1, column=0)
    bS.grid(padx=0,pady=5, row=1, column=1)
        
class Stack:
    def __init__(self):
        self.pila = []

    def estado(self):
        return len(self.pila) == 0

    def insertar(self, valor):
        self.pila.append(valor)

    def extraer(self):
        if not self.estado():
            return self.pila.pop()
        return None

    def consultar(self):
        if not self.estado():
            return self.pila[-1]
        return None

class Expresion:
    def __init__(self, x):
        self.expresion = x

    def esOperator(self, c):
        return c in "+-*/^"

    def precedente(self, operator):
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedences.get(operator, 0)

    def convertir_A_Postfija(self):
        stack = Stack()
        output = []
        for char in self.expresion:
            if char.isalnum():
                output.append(char)
            elif self.esOperator(char):
                while (not stack.estado() and
                       self.precedente(stack.consultar()) >= self.precedente(char)):
                    output.append(stack.extraer())
                stack.insertar(char)
            elif char == '(':
                stack.insertar(char)
            elif char == ')':
                while not stack.estado() and stack.consultar() != '(':
                    output.append(stack.extraer())
                stack.extraer()
        while not stack.estado():
            output.append(stack.extraer())
        return ''.join(output)

def menu2():
    g=impo()
    def accion():
        x=exe.get()
        expr = Expresion(x)
        postfi = expr.convertir_A_Postfija()
        messagebox.showinfo("",f"Infija: {x}\nPostfija: {postfi}")
    
    def salir():
        ventana.destroy()
        messagebox.showinfo("","Adios")
        g.menuPrincipal()
    
    ventana = tk.Tk()
    ventana.title("Convertir de Infija a Postfija")
    ventana.geometry("600x400+240+240")
    ex=tk.Label(ventana, text="Ingresa la Expresion a Convertir", justify="left", font=("Arial", 14))
    exe=tk.Entry(ventana)
    exe.grid(padx=0,pady=5, row=0, column=1)
    b1=tk.Button(ventana, text="Convertir", font=("Arial",14), command=accion)
    bS=tk.Button(ventana, text="Salir", font=("Arial",14), command=salir)
    ex.grid(pady=5, row=0, column=0)
    b1.grid(padx=0,pady=5, row=1, column=0)
    bS.grid(padx=0,pady=5, row=1, column=1)
    
    

  