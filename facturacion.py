import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Digifico
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UTN FRA")

        self.label_1 = tk.Label(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        self.txt_importe_1 = tk.Entry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = tk.Label(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        self.txt_importe_2 = tk.Entry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = tk.Label(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        self.txt_importe_3 = tk.Entry(master=self)
        self.txt_importe_3.grid(row=2, column=1)

        self.btn_total = tk.Button(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_promedio = tk.Button(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = tk.Button(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def get_prices(self):
        try:
            price_1 = float(self.txt_importe_1.get())
            price_2 = float(self.txt_importe_2.get())
            price_3 = float(self.txt_importe_3.get())
            return price_1, price_2, price_3
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def btn_total_on_click(self):
        prices = self.get_prices()
        if prices:
            total = sum(prices)
            messagebox.showinfo("Total", f"La suma total de los precios es: {total:.2f}")

    def btn_promedio_on_click(self):
        prices = self.get_prices()
        if prices:
            promedio = sum(prices) / len(prices)
            messagebox.showinfo("Promedio", f"El promedio de los precios es: {promedio:.2f}")

    def btn_total_iva_on_click(self):
        prices = self.get_prices()
        if prices:
            total_sin_iva = sum(prices)
            total_con_iva = total_sin_iva * 1.21  
            messagebox.showinfo("Total con IVA", f"El total con IVA es: {total_con_iva:.2f}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()