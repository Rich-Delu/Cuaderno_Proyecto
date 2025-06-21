import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class ContenedoresP1:
    def __init__(self):
        self.tupla= (3.2, 5.1, 7.6, 3.8, 5.1)
        self.lista= [3, 5, 7, 3, 5, 3, 3]
        self.conjunto= set(self.lista)
        self.diccionario= {num: num ** 2 for num in self.lista}

    def agregar_a_lista(self,ventana):
        def ejecutar_accion():
            x=int(t.get())
            self.lista.append(x)
            messagebox.showinfo("",f"Agregado {x} a la lista.")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        pre1=tk.Label(ventana, text="Agrega el elemento deseado:",font=("Arial", 10))
        pre1.grid(pady=5, row=0, column=0)
        t=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        t.grid(padx=5,pady=5, row=0, column=1)
        

    def eliminar_de_lista(self,ventana):
        def ejecutar_accion():
            x=int(t.get())
            if x in self.lista:
                self.lista.remove(x)
                messagebox.showinfo("",f"{x} Eliminado de la lista.")
            else:
                messagebox.showinfo("",f"{x} No se encuentra en la lista")
        
        def salir():
            ventana.destroy()
            self.menu()

        pre1=tk.Label(ventana, text="Escribe el elemento a eliminar:",font=("Arial", 10))
        pre1.grid(pady=5, row=0, column=0)
        t=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Eliminar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        t.grid(padx=5,pady=5, row=0, column=1)

    def agregar_elemeto_conjunto(self,ventana):
        def ejecutar_accion():
            x=int(t.get())
            if x in self.conjunto:
                messagebox.showinfo("",f"{x} Ya existe en el Conjunto.")
            else:
                self.conjunto.add(x)
                messagebox.showinfo("",f"{x} Agregado al Conjunto")
        
        def salir():
            ventana.destroy()
            self.menu()

        pre1=tk.Label(ventana, text="Escribe el elemento a agregar:",font=("Arial", 10))
        pre1.grid(pady=5, row=0, column=0)
        t=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Agregar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        t.grid(padx=5,pady=5, row=0, column=1)

    def eliminar_valor_conjunto(self, ventana):
        def ejecutar_accion():
            x=int(t.get())
            if x in self.conjunto:
                self.conjunto.remove(x)
                messagebox.showinfo("",f"{x} Eliminado del Conjunto.")
            else:
                messagebox.showinfo("",f"{x} No existe en el Conjunto")
        
        def salir():
            ventana.destroy()
            self.menu()

        pre1=tk.Label(ventana, text="Escribe el elemento a agregar:",font=("Arial", 10))
        pre1.grid(pady=5, row=0, column=0)
        t=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Eliminar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        t.grid(padx=5,pady=5, row=0, column=1)

    def ver(self,ventana):
        def salir():
            ventana.destroy()
            self.menu()
        
        Tupla=tk.Label(ventana, text=f"Tupla:{self.tupla}",font=("Arial", 10))
        Lista=tk.Label(ventana, text=f"Lista:{self.lista}",font=("Arial", 10))
        Conjunto=tk.Label(ventana, text=f"Conjunto:{self.conjunto}",font=("Arial", 10))
        Diccionario=tk.Label(ventana, text=f"Diccionario:{self.diccionario}",font=("Arial", 10))
        bS=tk.Button(ventana, text="Salir", command=salir)
        Tupla.grid(pady=5, row=0, column=0)
        Lista.grid(pady=5, row=1, column=0)
        Conjunto.grid(pady=5, row=2, column=0)
        Diccionario.grid(pady=5, row=3, column=0)
        bS.grid(padx=5, pady=5, row=4, column=1)

    def menu(self):
        g=impo()
        def ver_var():
            i=int(opc.get())
            titulo.destroy()
            op1.destroy()
            op2.destroy()
            op3.destroy()
            op4.destroy()
            op5.destroy()
            op6.destroy()    
            opc.destroy()
            b1.destroy()
            if i == 1:
                self.agregar_a_lista(ventana)
            elif i == 2:
                self.eliminar_de_lista(ventana)
            elif i == 3:
                self.agregar_elemeto_conjunto(ventana)
            elif i == 4:
                self.eliminar_valor_conjunto(ventana)
            elif i == 5:
                self.ver(ventana)
            elif i == 6:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Contenedores")
        ventana.geometry("500x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1.Agregar valores a la Lista", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Eliminar valores a la Lista", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Agregar elementos al conjunto", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Eliminar Valores al conjunto", justify="left", font=("Arial", 14))
        op5=tk.Label(ventana, text="5.Visualizar informacion", justify="left", font=("Arial",14))
        op6=tk.Label(ventana, text="6.Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=8, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=0, column=0)
        op1.grid(padx=0, pady=5, row=1, column=0)
        op2.grid(padx=0,pady=5, row=2, column=0)
        op3.grid(padx=0,pady=5, row=3, column=0)
        op4.grid(padx=0,pady=5, row=4, column=0)
        op5.grid(padx=0,pady=5,row=6, column=0)
        op6.grid(padx=0,pady=5,row=7, column=0)
        b1.grid(padx=0,pady=5, row=9, column=0)

class Temperatura:
    def __init__(self):
        self.temperaturas=[]

    def almacenar(self,ventana):
        def ejecutar_accion():
            x=int(t.get())
            self.temperaturas.append(x)
            messagebox.showinfo("",f"Agregado {x} a la lista.")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        pre1=tk.Label(ventana, text="Agrega las Temperaturas una despues de otra:",font=("Arial", 10))
        pre1.grid(pady=5, row=0, column=0)
        t=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        t.grid(padx=5,pady=5, row=0, column=1)

    def identificar(self,ventana):
        def salir():
            ventana.destroy()
            self.menu()
            
        tempUnicas = set(self.temperaturas)
        info=tk.Label(ventana, text=f"Las Temperaturas Unicas son: {tempUnicas}",font=("Arial", 10))
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=1, column=0)
        info.grid(row=0,column=0)

    def crearDiccionario(self, ventana):
        def salir():
            ventana.destroy()
            self.menu()
            
        diasSemana=[
            "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"
        ]
        ventana.geometry("800x400+240+240")
        tempDicc=dict(zip(diasSemana,self.temperaturas))
        info=tk.Label(ventana, text=f"Las Temperaturas Unicas son: {tempDicc}",font=("Arial", 10))
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=1, column=0)
        info.grid(row=0,column=0)

    def menu(self):
        g=impo()
        def ver_var():
            i=int(opc.get())
            titulo.destroy()
            op1.destroy()
            op2.destroy()
            op3.destroy()
            op4.destroy()
            opc.destroy()
            b1.destroy()
            if i == 1:
                self.almacenar(ventana)
            elif i == 2:
                self.identificar(ventana)
            elif i == 3:
                self.crearDiccionario(ventana)
            elif i == 4:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("")
        ventana.geometry("500x400+240+240")
        titulo=tk.Label(ventana, text="Aplicacion en un problema real", font=("Arial", 18))
        op1=tk.Label(ventana, text="1.Capturar Temperaturas", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Mostrar informacion de Temperaturas Unicas", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Mostrar Informacion de diccionario de Temperaturas", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=8, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=0, column=0)
        op1.grid(padx=0, pady=5, row=1, column=0)
        op2.grid(padx=0,pady=5, row=2, column=0)
        op3.grid(padx=0,pady=5, row=3, column=0)
        op4.grid(padx=0,pady=5, row=4, column=0)
        b1.grid(padx=0,pady=5, row=9, column=0)


