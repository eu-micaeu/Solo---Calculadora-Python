import tkinter as tk

# Função para calcular o resultado da expressão matemática
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Criando a entrada de texto
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Criando os botões
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: entry.insert(tk.END, "1"))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: entry.insert(tk.END, "2"))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: entry.insert(tk.END, "3"))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: entry.insert(tk.END, "4"))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: entry.insert(tk.END, "5"))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: entry.insert(tk.END, "6"))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: entry.insert(tk.END, "7"))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: entry.insert(tk.END, "8"))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: entry.insert(tk.END, "9"))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: entry.insert(tk.END, "0"))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: entry.insert(tk.END, "+"))
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=lambda: entry.insert(tk.END, "-"))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: entry.insert(tk.END, "*"))
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=lambda: entry.insert(tk.END, "/"))
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=calculate)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=lambda: entry.delete(0, tk.END))

# Posicionamento dos botões
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()