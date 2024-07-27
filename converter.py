import tkinter as tk
from tkinter import messagebox
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def convert_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        messagebox.showinfo("Conversion Result", f"{celsius}°C is equal to {fahrenheit}°F")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
def convert_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = fahrenheit_to_celsius(fahrenheit)
        messagebox.showinfo("Conversion Result", f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
root = tk.Tk()
root.title("Temperature Converter")
entry = tk.Entry(root, width=10)
entry.grid(row=0, column=1, padx=10, pady=10)
label = tk.Label(root, text="Enter Temperature:")
label.grid(row=0, column=0, padx=10, pady=10)
button_c_to_f = tk.Button(root, text="Celsius to Fahrenheit", command=convert_to_fahrenheit)
button_c_to_f.grid(row=1, column=0, padx=10, pady=10)
button_f_to_c = tk.Button(root, text="Fahrenheit to Celsius", command=convert_to_celsius)
button_f_to_c.grid(row=1, column=1, padx=10, pady=10)
root.mainloop()
