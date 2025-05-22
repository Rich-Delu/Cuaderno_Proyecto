import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class Cola:
    def __init__(self):
        self._cola=[]

    def ver(self, ventana):
        def salir():
            ventana.destroy()
            self.menu()
        
        elem=tk.Label(ventana, text=f"Los Elementos de la Pila son:{self._cola}",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=2, column=1)

    def insertar(self, ventana):
        def ejecutar_accion():
            x=int(el.get())
            self._cola.append(x)
            messagebox.showinfo("",f"Agregado {x} a la Pila.")
        
        def salir():
            ventana.destroy()
            self.menu ()
            
        elem=tk.Label(ventana, text="Agrega el elemento deseado a la Cola:",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        el=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        el.grid(padx=5,pady=5, row=0, column=1)

    def extraer(self):
        if not self.estado():
            self._cola.pop(0)
            messagebox.showinfo("",f"Ultimo Elemento Eliminado de la Cola.")
        else:
            messagebox.showinfo("",f"No hay Elementos en la Cola")

    def consultar(self):
        if not self.estado():
            self._cola[-1]
        return None

    def tamanio(self):
        if self._cola:
            x=len(self._cola)
            messagebox.showinfo("",f"Tamaño de la Cola:{x}.")
        else:
            messagebox.showinfo("",f"No hay Elementos en la Cola")

    def estado(self):
        return len(self._cola) == 0
    
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
                self.tamanio()
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
        ventana.title("Uso de Colas")
        ventana.geometry("600x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1.Insertar un elemento a la Cola", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Extraer un elemento de la Cola", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Consultar tamaño de la Cola", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Vizualizar elementos en la Cola", justify="left", font=("Arial", 14))
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

class Tareas:
    def __init__(self):
        self._tareas=[]
        self._tiempo=[]

    def leer(self, ventana):
        def ejecutar_accion():
            x=tare.get()
            y=int(hore.get())
            self._tareas.append(x)
            self._tiempo.append(y) 
            messagebox.showinfo("",f"{x} Agregado.")
        
        def salir():
            ventana.destroy()
            self.menu ()
            
        tar=tk.Label(ventana, text="Agrega la tarea que llego:",font=("Arial", 10))
        hor=tk.Label(ventana, text="Pon su tiempo estimado (min)")
        tar.grid(pady=5, row=0, column=0)
        hor.grid(pady=5, row=1, column=0)
        hore=tk.Entry(ventana)
        tare=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        tare.grid(padx=5,pady=5, row=0, column=1)
        hore.grid(padx=5, pady=5, row=1, column=1)

    def calcularTime(self):
        if self._tiempo:
            tiempoEstimado=sum(self._tiempo)
            messagebox.showinfo("",f"Tiempo estimado {tiempoEstimado} mins")
        else:
            messagebox.showinfo("",f"No hay Tareas guardadas")

    def atenderTarea(self):
        if not self.estado():
            messagebox.showinfo("",f"Tarea {self._tareas[0]} atendida")
            self._tareas.pop(-1)
            self._tiempo.pop(-1)
        else:
            messagebox.showinfo("",f"No hay tareas registradas")

    def tamanio(self):
        if not self.estado():
            messagebox.showinfo("",f"Numero de Tareas por atender:{len(self._tareas)}")
        else:
            messagebox.showinfo("",f"No hay tareas registradas")
            
    def estado(self):
        len(self._tareas) == 0
        len(self._tiempo) == 0

    def consultar(self,ventana):
        if not self.estado():
            def salir():
                ventana.destroy()
                self.menu ()
                
            tar=tk.Label(ventana, text=f"Tareas Registrar:{self._tareas}",font=("Arial", 10))
            hor=tk.Label(ventana, text=f"Tiempos de las tareas:{self._tiempo}")
            tar.grid(pady=5, row=0, column=0)
            hor.grid(pady=5, row=1, column=0)
            bS=tk.Button(ventana, text="Salir", command=salir)
            bS.grid(padx=5, pady=5, row=2, column=1)
        else:
            messagebox.showinfo("",f"No hay tareas registradas")

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
                op6.destroy()   
                opc.destroy()
                b1.destroy()
            i=int(opc.get())
            if i == 1:
                quitar()
                self.leer(ventana)
            elif i == 2:
                self.atenderTarea()
            elif i == 3:
                self.tamanio()
            elif i == 4:
                self.calcularTime()
            elif i == 5:
                quitar()
                self.consultar(ventana)
            elif i == 6:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Colas")
        ventana.geometry("600x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1.Insertar una Tarea", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Atender un tarea", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Consultar numero de tareas", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Calcular tiempo estimado", justify="left", font=("Arial", 14))
        op5=tk.Label(ventana, text="5.Visualizar tiempos y taras", justify="left", font=("Arial", 14))
        op6=tk.Label(ventana, text="6.Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=7, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=0, column=0)
        op1.grid(padx=0, pady=5, row=1, column=0)
        op2.grid(padx=0,pady=5, row=2, column=0)
        op3.grid(padx=0,pady=5, row=3, column=0)
        op4.grid(padx=0,pady=5, row=4, column=0)
        op5.grid(padx=0,pady=5,row=5, column=0)
        op6.grid(padx=0,pady=5,row=6, column=0)
        b1.grid(padx=0,pady=5, row=8, column=0)

