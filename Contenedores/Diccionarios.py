import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p

class Diccionario: 
    def __init__(self):
        self.diccionario = {}

    def insertar(self, ventana):
        def ejecutar_accion():
            x=ce.get()
            y=ve.get()
            self.diccionario[x] = y
            messagebox.showinfo("",f"Par clave-valor '{x}: {y}' insertado.")
        
        def salir():
            ventana.destroy()
            self.main()
            
        c=tk.Label(ventana, text="Introduce la Clave: ",font=("Arial", 10))
        v=tk.Label(ventana, text="Introduce el Valor: ",font=("Arial", 10))
        c.grid(pady=5, row=0, column=0)
        v.grid(pady=5, row=1, column=0)
        ce=tk.Entry(ventana)
        ve=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        ce.grid(padx=5,pady=5, row=0, column=1)
        ve.grid(padx=5,pady=5, row=1, column=1)

    def eliminar(self, ventana):
        def ejecutar_accion():
            x=ce.get()
            if x in self.diccionario:
                del self.diccionario[x]
                messagebox.showinfo("",f"Elemento con clave '{x}' eliminado.")
            else:
                messagebox.showinfo("",f"La clave '{x}' no se encuentra en el diccionario.")
        
        def salir():
            ventana.destroy()
            self.main()
            
        c=tk.Label(ventana, text="Introduce la Clave a Eliminar: ",font=("Arial", 10))
        c.grid(pady=5, row=0, column=0)
        ce=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Eliminar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        ce.grid(padx=5,pady=5, row=0, column=1)

    def buscar(self, ventana):
        def ejecutar_accion():
            x=ce.get()
            valor = self.diccionario.get(x)
            if valor is not None:
                messagebox.showinfo("",f"El valor para la clave '{x}' es: {valor}")
            else:
                messagebox.showinfo("",f"La clave '{x}' no se encuentra en el diccionario.")
        
        def salir():
            ventana.destroy()
            self.main()
            
        c=tk.Label(ventana, text="Introduce la Clave a Buscar: ",font=("Arial", 10))
        c.grid(pady=5, row=0, column=0)
        ce=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Buscar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        ce.grid(padx=5,pady=5, row=0, column=1)      

    def actualizar(self, ventana):
        def ejecutar_accion():
            def agregar():
                y=ve.get()
                self.diccionario[x] = y
                messagebox.showinfo("",f"El Valor {y} de la Clave {x} se ha actualizado")
            x=ce.get()
            if x in self.diccionario:
                v=tk.Label(ventana, text="Introduce el Nuevo Valor: ",font=("Arial", 10))
                v.grid(pady=5, row=1, column=0)
                ve=tk.Entry(ventana)
                ve.grid(padx=5,pady=5, row=1, column=1)
                bI=tk.Button(ventana, text="Actualizar", command=agregar)
                bI.grid(padx=5,pady=5, row=2, column=0)
            else:
                messagebox.showinfo("",f"{x} no se encuentra en el Diccionario")
        
        def salir():
            ventana.destroy()
            self.main()
            
        c=tk.Label(ventana, text="Introduce la Clave a Actualizar: ",font=("Arial", 10))
        c.grid(pady=5, row=0, column=0)
        ce=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Actualizar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        ce.grid(padx=5,pady=5, row=0, column=1)    

    def concatenar(self, ventana):
        def ejecutar_accion():
            x=ce.get()
            y=ve.get()
            otro_diccionario[x] = y
            messagebox.showinfo("",f"Par clave-valor '{x}: {y}' insertado.")
        
        def dics():
            self.diccionario.update(otro_diccionario)
            messagebox.showinfo("",f"Diccionario concatenado: {self.diccionario}")
            
        def salir():
            ventana.destroy()
            self.main()
        
        otro_diccionario = {}
        c=tk.Label(ventana, text="Introduce la Clave para el otro Diccionario: ",font=("Arial", 10))
        v=tk.Label(ventana, text="Introduce el Valor para el otro Diccionario: ",font=("Arial", 10))
        c.grid(pady=5, row=0, column=0)
        v.grid(pady=5, row=1, column=0)
        ce=tk.Entry(ventana)
        ve=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bD=tk.Button(ventana, text="Juntar los diccionarios", command=dics)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        bD.grid(padx=5,pady=5, row=3, column=0)
        ce.grid(padx=5,pady=5, row=0, column=1)
        ve.grid(padx=5,pady=5, row=1, column=1)

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
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Dicionarios")
        ventana.geometry("600x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1.Almacenar datos al Diccionario", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2.Eliminar datos del Diccionario", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3.Buscar un Elemento en el Diccionario", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4.Actualizar un elemento en el Diccionario", justify="left", font=("Arial", 14))
        op5=tk.Label(ventana, text="5.Concatenar otro Diccionario", justify="left", font=("Arial",14))
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
            
class RegistroEmpleados:
    def __init__(self):
        self.empleados = {
            "E001": {"nombre": "Carlos", "puesto": "Analista", "salario": 35000},
            "E002": {"nombre": "María", "puesto": "Desarrollador", "salario": 40000},
            "E003": {"nombre": "Elena", "puesto": "Gerente", "salario": 60000}
        }

    def agregar_empleado(self, ventana):
        def ejecutar_accion():
            x=ide.get()
            y=nome.get()
            z=puee.get()
            w=sale.get()
            if x in self.empleados:
                messagebox.showinfo("",f"El ID '{x}' ya existe. Usa otro ID.")
            else:
                self.empleados[x] = {"nombre": y, "puesto": z, "salario": w}
                messagebox.showinfo("",f"Empleado '{y}' agregado con ID '{x}'.")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        id=tk.Label(ventana, text="Ingresa el ID del empleado: ",font=("Arial", 10))
        nom=tk.Label(ventana, text="Ingresa el nombre del empleado: ",font=("Arial", 10))
        pue=tk.Label(ventana, text="Ingresa el puesto del empleado: ",font=("Arial", 10))
        sal=tk.Label(ventana, text="Ingresa el salario del empleado: ",font=("Arial", 10))
        id.grid(pady=5, row=0, column=0)
        nom.grid(pady=5, row=1, column=0)
        pue.grid(pady=5, row=2, column=0)
        sal.grid(pady=5, row=3, column=0)
        ide=tk.Entry(ventana)
        nome=tk.Entry(ventana)
        puee=tk.Entry(ventana)
        sale=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Insetar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=4, column=0)
        bS.grid(padx=5, pady=5, row=4, column=1)
        ide.grid(padx=5,pady=5, row=0, column=1)
        nome.grid(padx=5,pady=5, row=1, column=1)
        puee.grid(padx=5,pady=5, row=2, column=1)
        sale.grid(padx=5,pady=5, row=3, column=1)

    def actualizar_salario(self, ventana):
        def ejecutar_accion():
            def agregar():
                y=sale.get()
                self.empleados[x] = y
                messagebox.showinfo("",f"Se actualizo el Salario del Empleado:{x}")
            x=ide.get()
            if x in self.empleados:
                sal=tk.Label(ventana, text="Introduce el Nuevo Salario: ",font=("Arial", 10))
                sal.grid(pady=5, row=1, column=0)
                sale=tk.Entry(ventana)
                sale.grid(padx=5,pady=5, row=1, column=1)
                bI=tk.Button(ventana, text="Actualizar", command=agregar)
                bI.grid(padx=5,pady=5, row=2, column=0)
            else:
                messagebox.showinfo("",f"El Empleado con id {x} no se encuentra")

        def salir():
            ventana.destroy()
            self.menu()
            
        id=tk.Label(ventana, text="Ingresa el ID del empleado: ",font=("Arial", 10))
        id.grid(pady=5, row=0, column=0)
        ide=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Buscar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        ide.grid(padx=5,pady=5, row=0, column=1)

    def eliminar_empleado(self, ventana):
        def ejecutar_accion():
            x=ide.get()
            if x in self.empleados:
                del self.empleados[x]
                messagebox.showinfo("",f"El Empleado '{x}' a sido eliminado.")
            else:
                messagebox.showinfo("",f"El Empleado '{x}' no se encuentra registrado.")
        
        def salir():
            ventana.destroy()
            self.menu()
            
        id=tk.Label(ventana, text="Introduce ID del empleado a Eliminar: ",font=("Arial", 10))
        id.grid(pady=5, row=0, column=0)
        ide=tk.Entry(ventana)
        bI=tk.Button(ventana, text="Eliminar", command=ejecutar_accion)
        bS=tk.Button(ventana, text="Salir", command=salir)
        bI.grid(padx=5,pady=5, row=2, column=0)
        bS.grid(padx=5, pady=5, row=2, column=1)
        ide.grid(padx=5,pady=5, row=0, column=1)

    def listar_empleados(self, ventana):
        def salir():
            ventana.destroy()
            self.menu()
        
        if self.empleados:
            row_num = 0
            for id, datos in self.empleados.items():
                tk.Label(ventana, text=f"ID: {id}, Nombre: {datos['nombre']}, Puesto: {datos['puesto']}, Salario: {datos['salario']}", font=("Arial", 10)).grid(row=row_num, column=0, pady=2)
                row_num += 1
        else: 
            messagebox.showinfo("", "No hay empleados registrados")

        bS=tk.Button(ventana, text="Salir", command=salir)
        bS.grid(padx=5, pady=5, row=20, column=0)

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
            if i == 1:
                self.agregar_empleado(ventana)
            elif i == 2:
                self.actualizar_salario(ventana)
            elif i == 3:
                self.eliminar_empleado(ventana)
            elif i == 4:
                self.listar_empleados(ventana)
            elif i == 5:
                ventana.destroy()
                messagebox.showinfo("","Adios")
                g.menuPrincipal()
            else:
                messagebox.showinfo("","Opcion Invalida")
        ventana = tk.Tk()
        ventana.title("Uso de Dicionarios")
        ventana.geometry("600x400+240+240")
        titulo=tk.Label(ventana, text="Menu de Opciones", font=("Arial", 18))
        op1=tk.Label(ventana, text="1. Agregar empleado", justify="left", font=("Arial", 14))
        op2=tk.Label(ventana, text="2. Actualizar salario de empleado", justify="left", font=("Arial", 14))
        op3=tk.Label(ventana, text="3. Eliminar empleado", justify="left", font=("Arial", 14))
        op4=tk.Label(ventana, text="4. Listar empleados", justify="left", font=("Arial", 14))
        op5=tk.Label(ventana, text="5. Salir", justify="left", font=("Arial",14))
        opc=tk.Entry(ventana)
        opc.grid(padx=0,pady=5, row=9, column=0)
        b1=tk.Button(ventana, text="Aceptar", font=("Arial",14), command=ver_var)
        titulo.grid(pady=5, row=0, column=0)
        op1.grid(padx=0, pady=5, row=1, column=0)
        op2.grid(padx=0,pady=5, row=2, column=0)
        op3.grid(padx=0,pady=5, row=3, column=0)
        op4.grid(padx=0,pady=5, row=4, column=0)
        op5.grid(padx=0,pady=5,row=5, column=0)
        b1.grid(padx=0,pady=5, row=7, column=0)      