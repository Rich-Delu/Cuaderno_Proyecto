import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class ListasP1:
    def __init__(self):
        self.lista = [1, 2, 3, 4, 5]

    def insertar(self, ventana):
        def ejecutar_accion():
            x=int(el.get())
            y=int(po.get())
            self.lista.insert(y, x)
            messagebox.showinfo("",f"Agregado {x} a la lista.")
        
        def salir():
            ventana.destroy()
            self.main()
            
        elem=tk.Label(ventana, text="Agrega el elemento deseado:",font=("Arial", 10))
        pos=tk.Label(ventana, text="Introduce la posición en la que insertar el elemento:",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        pos.grid(pady=5, row=1, column=0)
        el=tk.Entry(ventana)
        po=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        el.grid(padx=5,pady=5, row=0, column=1)
        po.grid(padx=5,pady=5, row=1, column=1)

    def eliminar(self,ventana):
        def ejecutar_accion():
            x=int(el.get())
            if x in self.lista:
                self.lista.remove(x)
                messagebox.showinfo("",f"{x} Eliminado de la lista.")
            else:
                messagebox.showinfo("",f"{x} No esta en la Lista")
        
        def salir():
            ventana.destroy()
            self.main()
            
        elem=tk.Label(ventana, text="Pon el elemento a eliminar:",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        el=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        el.grid(padx=5,pady=5, row=0, column=1)

    def buscar(self, ventana):
        def ejecutar_accion():
            x=int(el.get())
            if x in self.lista:
                messagebox.showinfo("",f"El elemento {x} esta en la lista.")
            else:
                messagebox.showinfo("",f"El elemento {x} no esta en la lista.")
        
        def salir():
            ventana.destroy()
            self.main()
            
        elem=tk.Label(ventana, text="Introduce el elemento a buscar",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        el=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        el.grid(padx=5,pady=5, row=0, column=1)

    def actualizar(self, ventana):
        def ejecutar_accion():
            x=int(el.get())
            y=int(po.get())
            if y < len(self.lista):
                self.lista[y] = x
                messagebox.showinfo("",f"El elemento {x} se encuentra en la posición {y}")
            else:
                messagebox.showinfo("",f"La posición {y} es inválida.")
        
        def salir():
            ventana.destroy()
            self.main()
            
        pos=tk.Label(ventana, text="Introduce la posición del elemento a actualizar:",font=("Arial", 10))
        elem=tk.Label(ventana, text="Introduce el nuevo elemento:",font=("Arial", 10))
        elem.grid(pady=5, row=1, column=0)
        pos.grid(pady=5, row=0, column=0)
        po=tk.Entry(ventana)
        el=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        el.grid(padx=5,pady=5, row=1, column=1)
        po.grid(padx=5,pady=5, row=0, column=1)

    def concatenar(self, ventana):
        def ejecutar_accion():
            x=list(map(int, el.get().split()))
            self.lista += x
            messagebox.showinfo("",f"Las Listas fueron concatenadas")
        
        def salir():
            ventana.destroy()
            self.main()
            
        elem=tk.Label(ventana, text="Introduce la lista a concatenar (separada por espacios): ",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        el=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        el.grid(padx=5,pady=5, row=0, column=1)

    def ver(self,ventana):
        def salir():
            ventana.destroy()
            self.main()
            
        elem=tk.Label(ventana, text=f"La lista es:{self.lista}",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=1, column=0)

    def main(self):
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
            op7.destroy()    
            opc.destroy()
            b1.destroy()
            if i == 1:
                self.insertar(ventana)
            elif i == 2:
                self.eliminar(ventana)
            elif i == 3:
                self.buscar(ventana)
            elif i == 4:
                self.actualizar(ventana)
            elif i == 5:
                self.concatenar(ventana)
            elif i == 6:
                self.ver(ventana)
            elif i== 7:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Listas")
        ventana.geometry("600x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1.Insertar un elemento", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Eliminar un elemento", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Buscar un elemento", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Actualizar un elemento", justify="left", font=("Arial", 14))
        op5=tk.Label(ventana, text="5.Concatenar otra lista", justify="left", font=("Arial",14))
        op6=tk.Label(ventana, text="6.Visualizar lista", justify="left", font=("Arial",14))
        op7=tk.Label(ventana, text="7.Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=9, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=0, column=0)
        op1.grid(padx=0, pady=5, row=1, column=0)
        op2.grid(padx=0,pady=5, row=2, column=0)
        op3.grid(padx=0,pady=5, row=3, column=0)
        op4.grid(padx=0,pady=5, row=4, column=0)
        op5.grid(padx=0,pady=5,row=6, column=0)
        op6.grid(padx=0,pady=5,row=7, column=0)
        op7.grid(padx=0,pady=5,row=8, column=0)
        b1.grid(padx=0,pady=5, row=10, column=0)

class TemperaturaLi:
    def __init__(self):
        self.temperaturas = []

    def almacenar(self, ventana):
        def ejecutar_accion():
            x=int(el.get())
            self.temperaturas.append(x)
            messagebox.showinfo("",f"Agregado {x} a la lista de Temperaturas.")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        elem=tk.Label(ventana, text="Agrega las temperaturas una despuyes de otra:",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        el=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        el.grid(padx=5,pady=5, row=0, column=1)
        
    def agregar(self, ventana):
        def ejecutar_accion():
            x=int(el.get())
            self.temperaturas.append(x)
            messagebox.showinfo("",f"Agregado {x} a la lista de Temperaturas.")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        elem=tk.Label(ventana, text="Agrega la temperaturas nueva:",font=("Arial", 10))
        elem.grid(pady=5, row=0, column=0)
        el=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=1, column=0)
        bS.grid(padx=5, pady=5, row=1, column=1)
        el.grid(padx=5,pady=5, row=0, column=1)

    def eliminar(self, ventana):
        def ejecutar_accion():
            x=int(min.get())
            y=int(max.get())
            self.temperaturas = [temp for temp in self.temperaturas if x <= temp <= y]
            messagebox.showinfo("",f"Las temperatuas de {x} a {y} fueron eliminadas.")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        min_temp=tk.Label(ventana, text="Introduce la temperatura mínima para el rango: ",font=("Arial", 10))
        max_temp=tk.Label(ventana, text="Introduce la temperatura máxima para el rango:",font=("Arial", 10))
        min_temp.grid(pady=5, row=0, column=0)
        max_temp.grid(pady=5, row=1, column=0)
        min=tk.Entry(ventana)
        max=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        min.grid(padx=5,pady=5, row=0, column=1)
        max.grid(padx=5,pady=5, row=1, column=1)

    def encontrar(self, ventana):
        def ejecutar_accion():
            x=int(min_t.get())
            y=int(max_t.get())
            if x and y in self.temperaturas:
                y = max(self.temperaturas)
                x = min(self.temperaturas)
                messagebox.showinfo("",f"Temperatura más alta: {y} \n Temperatura más baja: {x}")
            else:
                messagebox.showinfo("","No hay temperaturas registradas.")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        min_temp=tk.Label(ventana, text="Introduce la temperatura mínima para el rango: ",font=("Arial", 10))
        max_temp=tk.Label(ventana, text="Introduce la temperatura máxima para el rango:",font=("Arial", 10))
        min_temp.grid(pady=5, row=0, column=0)
        max_temp.grid(pady=5, row=1, column=0)
        min_t=tk.Entry(ventana)
        max_t=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        min_t.grid(padx=5,pady=5, row=0, column=1)
        max_t.grid(padx=5,pady=5, row=1, column=1)

    def ver(self, ventana):
        def salir():
            ventana.destroy()
            self.menu()
            
        temps=tk.Label(ventana, text=f"Temperaturas registradas: {self.temperaturas}",font=("Arial", 10))
        temps.grid(pady=5, row=0, column=0)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=1, column=0)

    def ordenar(self):
        self.temperaturas.sort()
        messagebox.showinfo("",f"Las temperaturas fueron Ordenadas")

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
                op7.destroy()   
                opc.destroy()
                b1.destroy()
                
            i=int(opc.get())
            if i == 1:
                quitar()
                self.almacenar(ventana)
            elif i == 2:
                quitar()
                self.agregar(ventana)
            elif i == 3:
                quitar()
                self.eliminar(ventana)
            elif i == 4:
                quitar()
                self.encontrar(ventana)
            elif i == 5:
                self.ordenar()
            elif i == 6:
                quitar()
                self.ver(ventana)
            elif i == 7:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Listas")
        ventana.geometry("600x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1. Almacenar temperaturas iniciales", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2. Agregar una nueva temperatura", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3. Eliminar temperaturas fuera de un rango", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4. Encontrar la temperatura más alta y la más baja", justify="left", font=("Arial", 14))
        op5=tk.Label(ventana, text="5. Ordenar la lista de temperaturas", justify="left", font=("Arial",14))
        op6=tk.Label(ventana, text="6. Ver Temperaturas", justify="left", font=("Arial",14))
        op7=tk.Label(ventana, text="7. Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=9, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=0, column=0)
        op1.grid(padx=0, pady=5, row=1, column=0)
        op2.grid(padx=0,pady=5, row=2, column=0)
        op3.grid(padx=0,pady=5, row=3, column=0)
        op4.grid(padx=0,pady=5, row=4, column=0)
        op5.grid(padx=0,pady=5,row=6, column=0)
        op6.grid(padx=0,pady=5,row=7, column=0)
        op7.grid(padx=0,pady=5,row=8, column=0)
        b1.grid(padx=0,pady=5, row=10, column=0)