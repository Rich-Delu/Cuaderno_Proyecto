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
    def __init__(self):
        self.cola_clientes = queue.Queue()
        self.lock = threading.Lock()
        self.sem = threading.Semaphore(4)
        self.atendidos = 0

    def actualizar_info(self, msg):
        self.info.insert(tk.END, msg + "\n")


    def llegada_clientes(self, total,tl):
        for i in range(1, total +1):
            time.sleep(tl)
            cliente = f"Cliente-{i}"
            self.cola_clientes.put(cliente)
            with self.lock:
                self.ventana.after(0, self.actualizar_info,f"Llego {cliente} (En cola: {self.cola_clientes.qsize()})")

    def caja(self, numero):
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
    
    def simulador(self):
        total_clientes = int(self.Nce.get())
        tl=float(self.Tle.get())

        self.ventana.after(0, self.actualizar_info,tk.END, f"Dulceria CP")
        
        inicio = time.time()

        productor = threading.Thread(target=self.llegada_clientes, args=(total_clientes,tl,))
        productor.start()

        cajas =[
            threading.Thread(target=self.caja, args=(i,))
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

        self.ventana.after(0, self.actualizar_info,tk.END,"\n Todas los clientes fueron atendidos")
        self.ventana.after(0, self.actualizar_info,tk.END,f"Total de clientes atendidos: {dulceria.atendidos}")
        self.ventana.after(0, self.actualizar_info,tk.END,f"Tiempo total de atención: {tiempo_total:.2f} segundos")

    
    def menuPrincipal(self):
        def salir():
          self.ventana.destroy( )
          g=impo()
          messagebox.showinfo("","Adios")
          g.menuPrincipal()
            
        self.ventana = tk.Tk()
        self.ventana.title("")
        self.ventana.geometry("925x320+240+240")
        
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
        In=tk.Button(frame_Solicitar, text="Iniciar simulacion",command=self.simulador, font=("Arial", 14))
        bs=tk.Button(frame_Solicitar, text="Salir",command=salir, font=("Arial", 14))
        self.info=tk.Text(frame_Info, width=100, height=10)
        self.info.grid(row=0,column=0)
        titulo.grid(row=0, column=0, columnspan=5)
        Nc.grid(row=1, column=0)
        Tl.grid(row=1, column=2)
        Pr.grid(row=2, column=0)
        self.Nce.grid(row=1, column=1)
        self.Tle.grid(row=1, column=3)
        self.Pre.grid(row=2, column=1)
        In.grid(row=2, column=2)
        bs.grid(row=2, column=3)

        frame_Solicitar.columnconfigure(1, weight=1)
        frame_Solicitar.rowconfigure(1, weight=1)
        frame_Solicitar.rowconfigure(2, weight=1)

        self.ventana.mainloop()
        
    