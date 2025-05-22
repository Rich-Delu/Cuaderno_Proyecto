import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class ConjuntosP1:
    def __init__(self):
        self.conjunto_b = set()
        self.conjunto_a = set()

    def crear(self, ventana):
        def ejecutar_accion():
            x=int(ca.get())
            y=int(cb.get())
            self.conjunto_a.add(x)
            self.conjunto_b.add(y)
            messagebox.showinfo("",f"Los Elementos agregados a los conjuntos Conjuntos")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        c_a=tk.Label(ventana, text="Introduce el elemento del conjunto A: ",font=("Arial", 10))
        c_b=tk.Label(ventana, text="Introduce el elemento del conjunto B: ",font=("Arial", 10))
        c_a.grid(pady=5, row=0, column=0)
        c_b.grid(pady=5, row=1, column=0)
        ca=tk.Entry(ventana)
        cb=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        ca.grid(padx=5,pady=5, row=0, column=1)
        cb.grid(padx=5,pady=5, row=1, column=1)

    def union(self, ventana):
        def salir():
            ventana.destroy()
            self.menu()
        
        union= self.conjunto_a | self.conjunto_b
        res=tk.Label(ventana, text=f"Union de conjuntos:{union}" ,font=("Arial", 10)) 
        res.grid(pady=5, row=0, column=0)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=5, column=0)

    def diferencia(self,ventana):
        def salir():
            ventana.destroy()
            self.menu()
        
        dif=self.conjunto_a - self.conjunto_b
        res=tk.Label(ventana, text=f"Diferencia entre conjuntos:{dif}" ,font=("Arial", 10)) 
        res.grid(pady=5, row=0, column=0)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=5, column=0)

    def complemento(self, ventana):
        def salir():
            ventana.destroy()
            self.menu()
        
        comp = self.conjunto_a ^ self.conjunto_b
        res=tk.Label(ventana, text=f"Diferencia simétrica entre conjuntos:{comp}" ,font=("Arial", 10)) 
        res.grid(pady=5, row=0, column=0)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=5, column=0)

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
            opc.destroy()
            b1.destroy()
            c1.destroy()
            c2.destroy()
            if i == 1:
                self.crear(ventana)
            elif i == 2:
                self.union(ventana)
            elif i == 3:
                self.diferencia(ventana)
            elif i == 4:
                self.complemento(ventana)
            elif i == 5:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Listas")
        ventana.geometry("700x600+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        c1=tk.Label(ventana, text=f"Conjunto A:{self.conjunto_a}", justify="left", font=("Arial", 14))
        c2=tk.Label(ventana, text=f"Conjunto B:{self.conjunto_b}", justify="left", font=("Arial", 14))
        op1=tk.Label(ventana, text="1.Crear los conjuntos", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Unión de dos conjuntos", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Diferencia entre dos conjuntos", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Diferencia simétrica (complemento) entre dos conjuntos", justify="left", font=("Arial",14))
        op5=tk.Label(ventana, text="5.Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=8, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=2, column=0)
        op1.grid(padx=0, pady=5, row=3, column=0)
        op2.grid(padx=0,pady=5, row=4, column=0)
        op3.grid(padx=0,pady=5, row=5, column=0)
        op4.grid(padx=0,pady=5, row=6, column=0)
        op5.grid(padx=0,pady=5,row=7, column=0)
        b1.grid(padx=0,pady=5, row=9, column=0)
        c1.grid(pady=5, row=0, column=0)
        c2.grid(pady=5, row=1, column=0)

class Alumnos:
    def __init__(self):
        self.curso1 = set()
        self.curso2 = set()

    def almacenar(self,ventana):
        def ejecutar_accion():
            x=ca.get()
            y=cb.get()
            self.curso1.add(x)
            self.curso2.add(y)
            messagebox.showinfo("",f"Los Elementos agregados a los conjuntos Conjuntos")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        c_a=tk.Label(ventana, text="Introduce el nombre del alumno a agregar al Curso 1: ",font=("Arial", 10))
        c_b=tk.Label(ventana, text="Introduce el nombre del alumno a agregar al Curso 2: ",font=("Arial", 10))
        c_a.grid(pady=5, row=0, column=0)
        c_b.grid(pady=5, row=1, column=0)
        ca=tk.Entry(ventana)
        cb=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        ca.grid(padx=5,pady=5, row=0, column=1)
        cb.grid(padx=5,pady=5, row=1, column=1)  

    def encontrarDuplicado(self,ventana):
        def salir():
            ventana.destroy()
            self.menu()
            
        duplicado=self.curso1 & self.curso2
        res=tk.Label(ventana, text=f"Alumnos en ambos cursos:{duplicado}",font=("Arial", 10)) 
        bS=tk.Button(ventana, text="Salir", command=salir)
        res.grid(row=0, column=0)
        bS.grid(padx=5, pady=5, row=1, column=0)

    def encontrarExclusivos(self,ventana):
        def salir():
            ventana.destroy()
            self.menu()
            
        exclusivos1 = self.curso1 - self.curso2
        exclusivos2 = self.curso2 - self.curso1
        c1=tk.Label(ventana, text=f"Alumnos exclusivos de curso 1:{exclusivos1}",font=("Arial", 10)) 
        c2=tk.Label(ventana, text=f"Alumnos exclusivos de curso 2:{exclusivos2}",font=("Arial", 10))
        bS=tk.Button(ventana, text="Salir", command=salir)
        c1.grid(row=0, column=0)
        c2.grid(row=1, column=0)
        bS.grid(padx=5, pady=5, row=2, column=0)
        
    def alumnosDuplicados(self,ventana):
        def salir():
            ventana.destroy()
            self.menu()
            
        total_alumnos = len(self.curso1 & self.curso2)      
        c1=tk.Label(ventana, text=f"Total de alumnos duplicados:{total_alumnos}",font=("Arial", 10)) 
        bS=tk.Button(ventana, text="Salir", command=salir)
        c1.grid(row=0, column=0)
        bS.grid(padx=5, pady=5, row=1, column=0)

    def alumnosNoDuplicados(self,ventana):
        def salir():
            ventana.destroy()
            self.menu()
            
        total_alumnos = len(self.curso1 | self.curso2) 
        c1=tk.Label(ventana, text=f"Total de alumnos sin duplicados:{total_alumnos}",font=("Arial", 10)) 
        bS=tk.Button(ventana, text="Salir", command=salir)
        c1.grid(row=0, column=0)
        bS.grid(padx=5, pady=5, row=1, column=0)

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
                self.almacenar(ventana)
            elif i == 2:
                self.encontrarDuplicado(ventana)
            elif i == 3:
                self.encontrarExclusivos(ventana)
            elif i == 4:
                self.alumnosDuplicados(ventana)
            elif i == 5:
                self.alumnosNoDuplicados(ventana)
            elif i == 6:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Listas")
        ventana.geometry("600x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1.Almacenar alumnos en cada curso", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Encontrar alumnos inscritos en ambos cursos", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Encontrar alumnos exclusivos de cada curso", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Obtener total de alumnos duplicados", justify="left", font=("Arial", 14))
        op5=tk.Label(ventana, text="5.Obtener total de alumnos sin duplicados", justify="left", font=("Arial",14))
        op6=tk.Label(ventana, text="6.Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=9, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=0, column=0)
        op1.grid(padx=0, pady=5, row=1, column=0)
        op2.grid(padx=0,pady=5, row=2, column=0)
        op3.grid(padx=0,pady=5, row=3, column=0)
        op4.grid(padx=0,pady=5, row=4, column=0)
        op5.grid(padx=0,pady=5,row=5, column=0)
        op6.grid(padx=0,pady=5,row=6, column=0)
        b1.grid(padx=0,pady=5, row=7, column=0)