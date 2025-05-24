from Contenedores.Cont import ContenedoresP1, Temperatura
from Contenedores.Diccionarios import Diccionario, RegistroEmpleados
from Contenedores.Listas import ListasP1, TemperaturaLi
from Contenedores.Conjuntos import ConjuntosP1, Alumnos
from Colas_y_Pilas.Colas import Cola, Tareas
from Colas_y_Pilas.Pilas import Pila1, menu1, menu2
from Recur_Grafos.Recursividad import menu1_R, menu2_R
from Recur_Grafos.Grafos import Aeropuertos
from AeroPaletas.Grafos_AeroPaletas import Aeropuertos_1
import tkinter as tk
from tkinter import messagebox
 
class AP:
    def ContenedoresMen(self, x):
        self.ventana.destroy()
        if x==1:
                def ejecutar_accion():
                    nonlocal ventana_abierta
                    if not ventana_abierta:
                        ventana_abierta = True
                        if y.get() == 1:
                            ventanaP1.destroy()
                            c1 = ContenedoresP1()
                            c1.menu()
                        elif y.get() == 2:
                            ventanaP1.destroy()
                            c2 = Temperatura()
                            c2.menu()    
                ventanaP1 = tk.Tk()
                ventanaP1.title("Practica 1 (Estructuras de Datos y Contenedores en Python")
                ventanaP1.geometry("500x400+240+240")
                y=tk.IntVar(value=0)
                ventana_abierta = False
                p1=tk.Label(ventanaP1, text="Actividad 1", font=("Arial", 14)).grid(padx=40, row=3, column=1)
                p2=tk.Label(ventanaP1, text="Acttividad 2", font=("Arial", 14)).grid(padx=20, row=3, column=3)
                titulo=tk.Label(ventanaP1, text="Actividades", font=("Arial", 18)).grid(pady=5, row=0, column=2)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(1), ejecutar_accion()]).grid(padx=40, row=4, column=1)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(2), ejecutar_accion()]).grid(padx=20, row=4, column=3)
        elif x==2:
                def ejecutar_accion(y):
                    nonlocal ventana_abierta
                    if not ventana_abierta:
                        ventana_abierta = True
                        if y == 1:
                            ventanaP1.destroy()
                            l1 = ListasP1()
                            l1.main()
                        elif y == 2:
                            ventanaP1.destroy()
                            l2 = TemperaturaLi()
                            l2.menu()    
                ventanaP1 = tk.Tk()
                ventanaP1.title("Practica 2 (Listas)")
                ventanaP1.geometry("500x400+240+240")
                y=tk.IntVar(value=0)
                ventana_abierta = False
                p1=tk.Label(ventanaP1, text="Actividad 1", font=("Arial", 14)).grid(padx=40, row=3, column=1)
                p2=tk.Label(ventanaP1, text="Acttividad 2", font=("Arial", 14)).grid(padx=20, row=3, column=3)
                titulo=tk.Label(ventanaP1, text="Actividades", font=("Arial", 18)).grid(pady=5, row=0, column=2)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda:ejecutar_accion(1)).grid(padx=40, row=4, column=1)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda:ejecutar_accion(2)).grid(padx=20, row=4, column=3)
        elif x==3:
                def ejecutar_accion(y):
                    nonlocal ventana_abierta
                    if not ventana_abierta:
                        ventana_abierta = True
                        if y == 1:
                            ventanaP1.destroy()
                            Con1 = ConjuntosP1()
                            Con1.menu()
                        elif y == 2:
                            ventanaP1.destroy()
                            Con2 = Alumnos()
                            Con2.menu()    
                ventanaP1 = tk.Tk()
                ventanaP1.title("Practica 3 (Conjuntos)")
                ventanaP1.geometry("500x400+240+240")
                y=tk.IntVar(value=0)
                ventana_abierta = False
                p1=tk.Label(ventanaP1, text="Actividad 1", font=("Arial", 14)).grid(padx=40, row=3, column=1)
                p2=tk.Label(ventanaP1, text="Acttividad 2", font=("Arial", 14)).grid(padx=20, row=3, column=3)
                titulo=tk.Label(ventanaP1, text="Actividades", font=("Arial", 18)).grid(pady=5, row=0, column=2)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda:ejecutar_accion(1)).grid(padx=40, row=4, column=1)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda:ejecutar_accion(2)).grid(padx=20, row=4, column=3)
        elif x==4:
                def ejecutar_accion(y):
                    nonlocal ventana_abierta
                    if not ventana_abierta:
                        ventana_abierta = True
                        if y == 1:
                            ventanaP1.destroy()
                            Dic1 = Diccionario()
                            Dic1.main()
                        elif y == 2:
                            ventanaP1.destroy()
                            Dic2 = RegistroEmpleados()
                            Dic2.menu()    
                ventanaP1 = tk.Tk()
                ventanaP1.title("Practica 4 (Diccionarios)")
                ventanaP1.geometry("500x400+240+240")
                y=tk.IntVar(value=0)
                ventana_abierta = False
                p1=tk.Label(ventanaP1, text="Actividad 1", font=("Arial", 14)).grid(padx=40, row=3, column=1)
                p2=tk.Label(ventanaP1, text="Acttividad 2", font=("Arial", 14)).grid(padx=20, row=3, column=3)
                titulo=tk.Label(ventanaP1, text="Actividades", font=("Arial", 18)).grid(pady=5, row=0, column=2)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda:ejecutar_accion(1)).grid(padx=40, row=4, column=1)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda:ejecutar_accion(2)).grid(padx=20, row=4, column=3)

    def Colas_y_Pilas(self,x):
        self.ventana.destroy()
        if x==1:
                def ejecutar_accion():
                    nonlocal ventana_abierta
                    if not ventana_abierta:
                        ventana_abierta = True
                        if y.get() == 1:
                            ventanaP1.destroy()
                            p1 = Pila1()
                            p1.menu()
                        elif y.get() == 2:
                            ventanaP1.destroy()
                            menu1()
                        elif y.get() == 3:
                            ventanaP1.destroy()
                            menu2()
                
                ventanaP1 = tk.Tk()
                ventanaP1.title("Practica 2.1 (Pilas)")
                ventanaP1.geometry("500x400+240+240")
                y=tk.IntVar(value=0)
                ventana_abierta = False
                p1=tk.Label(ventanaP1, text="Actividad 1", font=("Arial", 14)).grid(padx=20, row=3, column=1)
                p2=tk.Label(ventanaP1, text="Actividad 2", font=("Arial", 14)).grid(padx=20, row=3, column=2)
                p3=tk.Label(ventanaP1, text="Actividad 3", font=("Arial", 14)).grid(padx=20, row=3, column=3)
                titulo=tk.Label(ventanaP1, text="Actividades", font=("Arial", 18)).grid(pady=5, row=0, column=2)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(1), ejecutar_accion()]).grid(padx=40, row=4, column=1)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(2), ejecutar_accion()]).grid(padx=20, row=4, column=2)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(3), ejecutar_accion()]).grid(padx=20, row=4, column=3)
        elif x==2:
                def ejecutar_accion():
                    nonlocal ventana_abierta
                    if not ventana_abierta:
                        ventana_abierta = True
                        if y.get() == 1:
                            ventanaP1.destroy()
                            c1 = Cola()
                            c1.menu()
                        elif y.get() == 2:
                            ventanaP1.destroy()
                            c2 = Tareas()
                            c2.menu()  
                ventanaP1 = tk.Tk()
                ventanaP1.title("Practica 2.2 (Colas)")
                ventanaP1.geometry("500x400+240+240")
                y=tk.IntVar(value=0)
                ventana_abierta = False
                p1=tk.Label(ventanaP1, text="Actividad 1", font=("Arial", 14)).grid(padx=20, row=3, column=1)
                p2=tk.Label(ventanaP1, text="Actividad 2", font=("Arial", 14)).grid(padx=20, row=3, column=3)
                titulo=tk.Label(ventanaP1, text="Actividades", font=("Arial", 18)).grid(pady=5, row=0, column=2)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(1), ejecutar_accion()]).grid(padx=40, row=4, column=1)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(2), ejecutar_accion()]).grid(padx=20, row=4, column=3)

    def Recur_y_Grafo(self, x):
        self.ventana.destroy()
        if x==1:
                def ejecutar_accion():
                    nonlocal ventana_abierta
                    if not ventana_abierta:
                        ventana_abierta = True
                        if y.get() == 1:
                            ventanaP1.destroy()
                            menu1_R()
                        elif y.get() == 2:
                            ventanaP1.destroy()
                            menu2_R()
                
                ventanaP1 = tk.Tk()
                ventanaP1.title("Practica 3.1 (Recusividad)")
                ventanaP1.geometry("500x400+240+240")
                y=tk.IntVar(value=0)
                ventana_abierta = False
                p1=tk.Label(ventanaP1, text="Actividad 1", font=("Arial", 14)).grid(padx=20, row=3, column=1)
                p2=tk.Label(ventanaP1, text="Actividad 2", font=("Arial", 14)).grid(padx=20, row=3, column=3)
                titulo=tk.Label(ventanaP1, text="Actividades", font=("Arial", 18)).grid(pady=5, row=0, column=2)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(1), ejecutar_accion()]).grid(padx=40, row=4, column=1)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=lambda: [y.set(2), ejecutar_accion()]).grid(padx=20, row=4, column=3)
        elif x==2:
                def ejecutar_accion():
                    c1 = Aeropuertos()
                    c1.mostrar()
                def salir():
                    ventanaP1.destroy()
                    self.menuPrincipal()
                ventanaP1 = tk.Tk()
                ventanaP1.title("Practica 3.2 (Grafos)")
                ventanaP1.geometry("500x400+240+240")
                y=tk.IntVar(value=0)
                ventana_abierta = False
                titulo=tk.Label(ventanaP1, text="Grafo de Viajes y Aerolineas", font=("Arial", 18)).grid(pady=5, row=0, column=0)
                tk.Button(ventanaP1, text="Ejecutar", font=("Arial", 14), command=ejecutar_accion).grid(padx=40, row=1, column=0)
                tk.Button(ventanaP1, text="Salir", font=("Arial", 14), command=salir).grid(padx=40, row=2, column=0)
        
    def Aeropal(self):
        self.ventana.destroy()
        aer=Aeropuertos_1()
        aer.menuPrincipal()        
 
    def salir(self):
        self.ventana.destroy()

    def acerca_de(self):
        messagebox.showinfo("Acerca del Alumno", "Alumno: Delucio Fuentes Ricardo Ismael")

    def menuPrincipal(self):
        self.ventana = tk.Tk()
        self.ventana.title("Examen")
        self.ventana.geometry("900x300+240+240")
        menu_principal=tk.Menu(self.ventana)

        menu_Contenedores = tk.Menu(menu_principal, tearoff=0)
        menu_Contenedores.add_command(label="Practica 1 (Estructuras de Datos y Contenedores en Python)", command=lambda:self.ContenedoresMen(1))
        menu_Contenedores.add_command(label="Practica 2 (Listas)", command=lambda:self.ContenedoresMen(2))
        menu_Contenedores.add_command(label="Practica 3 (Conjuntos)", command=lambda:self.ContenedoresMen(3))
        menu_Contenedores.add_command(label="Practica 4 (Diccionarios)", command=lambda:self.ContenedoresMen(4))

        menu_Colas_Pilas = tk.Menu(menu_principal, tearoff=0)
        menu_Colas_Pilas.add_command(label="Practica 2.1 (Pilas)", command=lambda:self.Colas_y_Pilas(1))
        menu_Colas_Pilas.add_command(label="Practica 2.2 (Colas)", command=lambda:self.Colas_y_Pilas(2))
        
        menu_Recur_Grafo = tk.Menu(menu_principal, tearoff=0)
        menu_Recur_Grafo.add_command(label="Practica 3.1 (Recursividad)", command=lambda:self.Recur_y_Grafo(1))
        menu_Recur_Grafo.add_command(label="Practica 3.2 (Grafos)", command=lambda:self.Recur_y_Grafo(2))

        menu_principal.add_cascade(label="Contenedores", menu=menu_Contenedores)
        menu_principal.add_cascade(label="Colas y Pilas", menu=menu_Colas_Pilas)
        menu_principal.add_cascade(label="Recursividad y Grafos", menu=menu_Recur_Grafo)
        menu_principal.add_cascade(label="Proyecto (AeroPaletas)", command=self.Aeropal)
        menu_principal.add_cascade(label="Acerca de", command=self.acerca_de)       
        menu_principal.add_cascade(label="Salir", command=self.salir)

        titulo=tk.Label(self.ventana, text="Cuaderno de Evidencias para el Segundo Parcial", font=("Arial", 18))
        intro=tk.Label(self.ventana, text="En este programa estan todas las practicas hechas y  guardadas en distintos menus", font=("Arial", 14))
        titulo.grid(row=0, column=5)
        intro.grid(row=1, column=5)
        self.ventana.config(menu=menu_principal)

        self.ventana.mainloop()

if __name__=='__main__':
    pro=AP()
    pro.menuPrincipal()