import threading
import queue
import time
import random
import tkinter as tk
from tkinter import messagebox

def impo():
    import Proyecto_2do_Parcial as Proy
    p=Proy.AP()
    return p


class DulceriaCP:
    def __init__(self,OP):
        self.cola_clientes = queue.Queue()
        self.lock = threading.Lock()
        self.OP = OP
        if self.OP == 4:
            self.sem = threading.Semaphore(4)
        elif self.OP != 4:
            self.sem = threading.Semaphore(self.OP)
        self.atendidos = 0

    def actualizar_info(self, msg):
        self.info.insert(tk.END, msg + "\n")
    
    def actu_time(self, tm):
        if self.OP == 3:
            self.CON3.config(text=f"Tiempo en Tardar con 3 Hilos: {tm:.2f} segundos")
        elif self.OP == 5:
            self.CON5.config(text=f"Tiempo en Tardar con 5 Hilos: {tm:.2f} segundos")

    def llegada_clientes(self, total,tl):
        for i in range(1, total +1):
            time.sleep(tl)
            cliente = f"Cliente-{i}"
            self.cola_clientes.put(cliente)
            with self.lock:
                self.ventana.after(0, self.actualizar_info,f"Llego {cliente} (En cola: {self.cola_clientes.qsize()})")

    def caja_sec(self,numero,alumno, tl):
        self.info.insert(tk.END, f"\nVentanilla {numero} atiende a {alumno}")
        time.sleep(tl)
        self.info.insert(tk.END, f"\nVentanilla {numero} ha terminado con alumno {alumno}")

    def caja_con(self, numero):
        while True:
            try:
                cliente =self.cola_clientes.get(timeout=2)
            except queue.Empty:
                break

            if not self.sem.acquire(timeout=1):
                with self.lock:
                    self.ventana.after(0, self.actualizar_info,f"[Caja,-{numero}] No pudo atender a {cliente} (timeout)")
                continue

            try:
                with self.lock:
                    self.ventana.after(0, self.actualizar_info,f"[Caja-{numero}] Atendiendo a {cliente}")
                time.sleep(random.uniform(0.5,1.0))

                with self.lock:
                    self.atendidos+=1
                    self.ventana.after(0, self.actualizar_info,f"[Caja-{numero}] Termino con {cliente} | Total atendidos: {self.atendidos}")
            finally:
                self.sem.release()
                self.cola_clientes.task_done()

    def simulador_sec(self, tc,tl,pre):
        self.info.delete("1.0", tk.END)
        self.info.insert(tk.END, f"Programa Secuencial")
        inicio = time.time()
        for i in range(tc):
            self.caja_sec(i, f"Cliente{i}",tl)
        fin = time.time()

        tiempo_total = fin - inicio
        to= tc*pre
        self.info.insert(tk.END, f"\nTiempo en Tardar:{tiempo_total:.2f}")
        self.info.insert(tk.END, f"\nTotal Ganada:{to}")
        self.SEC.config(text=f"Tiempo en Tardar modo Secuencial:{tiempo_total:.2f} segundos")

    def simulador_con(self,tc,tl,pre):
        self.info.delete("1.0", tk.END)

        self.ventana.after(0, self.actualizar_info, f"Dulceria CP")

        inicio = time.time()

        productor = threading.Thread(target=self.llegada_clientes, args=(tc,tl,))
        productor.start()

        cajas =[
            threading.Thread(target=self.caja_con, args=(i,))
            for i in range(1,7)
        ]

        for c in cajas:
            c.start()

        productor.join()
        self.cola_clientes.join()
        for c in cajas:
            c.join()

        fin = time.time()

        tiempo_total = fin - inicio

        tg= pre * self.atendidos

        self.ventana.after(0, self.actualizar_info,"\nTodas los clientes fueron atendidos")
        self.ventana.after(0, self.actualizar_info,f"Total de clientes atendidos: {self.atendidos}")
        self.ventana.after(0, self.actualizar_info,f"Total de Dinero Obtenido: {tg}$")
        self.ventana.after(0, self.actualizar_info,f"Tiempo total de atención: {tiempo_total:.2f} segundos")
        self.ventana.after(0, self.actu_time, tiempo_total)

    def menuPrincipal(self):
        def pros_acc(x):
            try:
                tc = int(self.Nce.get())
                tl = float(self.Tle.get())
                pre = int(self.Pre.get())
            except ValueError:
                messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")
                return

            if x == 1:
                nueva = DulceriaCP(3)
            elif x == 2:
                nueva = DulceriaCP(5)
            elif x == 3:
                nueva = DulceriaCP(4)
                
            nueva.ventana = self.ventana
            nueva.info = self.info
            nueva.CON3 = self.CON3
            nueva.CON5 = self.CON5
            nueva.SEC = self.SEC
            
            if x in (1, 2):
                threading.Thread(target=nueva.simulador_con, args=(tc, tl, pre)).start()
            elif x == 3:
                threading.Thread(target=nueva.simulador_sec, args=(tc, tl, pre)).start()
        
        def salir():
          self.ventana.destroy( )
          g=impo()
          messagebox.showinfo("","Adios")
          g.menuPrincipal()

        self.ventana = tk.Tk()
        self.ventana.title("")
        self.ventana.geometry("1310x320+240+240")

        frame_Solicitar = tk.Frame(self.ventana, padx=10, pady=10)
        frame_Solicitar.grid(row=0, column=0, columnspan=5, sticky="nsew")
        frame_Info = tk.Frame(self.ventana, padx=10, pady=10)
        frame_Info.grid(row=1, column=0, columnspan=5, sticky="nsew")

        titulo=tk.Label(frame_Solicitar, text="Bienvenido a CineCD", font=("Arial", 18))
        Nc=tk.Label(frame_Solicitar, text="Numero de Clientes", font=("Arial", 14))
        Tl=tk.Label(frame_Solicitar, text="Tiempo de llegada de cada Cliente (seg)", font=("Arial", 14))
        Pr=tk.Label(frame_Solicitar, text="Precio del Boleto", font=("Arial", 14))
        self.Nce=tk.Entry(frame_Solicitar)
        self.Tle=tk.Entry(frame_Solicitar)
        self.Pre=tk.Entry(frame_Solicitar)
        Con3=tk.Button(frame_Solicitar, text="Iniciar simulacion Concurrente con 3 Hilos",command=lambda:pros_acc(1) , font=("Arial", 14))
        Con5=tk.Button(frame_Solicitar, text="Iniciar simulacion Concurrente con 5 Hilos",command=lambda:pros_acc(2) , font=("Arial", 14))
        Sec=tk.Button(frame_Solicitar, text="Iniciar simulacion Secuencial",command=lambda:pros_acc(3) , font=("Arial", 14))
        bs=tk.Button(frame_Solicitar, text="Salir",command=salir, font=("Arial", 14))
        self.info=tk.Text(frame_Info, width=100, height=10)
        self.CON3=tk.Label(frame_Info, text="Tiempo en Tardar con 3 Hilos:", font=("Arial", 14))
        self.CON5=tk.Label(frame_Info, text="Tiempo en Tardar con 5 Hilos:", font=("Arial", 14))
        self.SEC=tk.Label(frame_Info, text="Tiempo en Tardar modo Secuencial:", font=("Arial", 14))
        self.info.grid(row=0,column=0,rowspan=3)
        self.CON3.grid(row=0, column=2)
        self.CON5.grid(row=1, column=2)
        self.SEC.grid(row=2, column=2)
        scrollbar = tk.Scrollbar(frame_Info, command=self.info.yview)
        self.info.config(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        titulo.grid(row=0, column=0, columnspan=5)
        Nc.grid(row=1, column=0)
        Tl.grid(row=1, column=2)
        Pr.grid(row=2, column=0)
        self.Nce.grid(row=1, column=1)
        self.Tle.grid(row=1, column=3)
        self.Pre.grid(row=2, column=1)
        Con3.grid(row=2, column=2)
        Con5.grid(row=2, column=3)
        Sec.grid(row=2, column=4)
        bs.grid(row=1, column=4)

        frame_Solicitar.columnconfigure(1, weight=1)
        frame_Solicitar.rowconfigure(1, weight=1)
        frame_Solicitar.rowconfigure(2, weight=1)

        self.ventana.mainloop()