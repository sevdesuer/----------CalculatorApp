import tkinter as tk 
import math

def on_button_click(symbol): 
    if symbol == "C": 
        entry.delete(0, tk.END) 
        
    elif symbol == "=":
        try:
            # "x^y" yerine "**" kullanıyoruz
            expression = entry.get().replace("x", "*").replace("÷", "/").replace("x^y", "**")
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif symbol == "√":
        try:
            value = float(entry.get()) if entry.get() else 0
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(math.sqrt(value)))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif symbol == "←":
        entry.delete(len(entry.get())-1, tk.END)

    elif symbol == ",":
        if "." not in entry.get():
            entry.insert(tk.END, ".")

    elif symbol == "x^y":
        # Burada "x^y" yerine direkt "**" ekliyoruz
        entry.insert(tk.END, "**")

    else:
        entry.insert(tk.END, symbol)

# Tkinter de pencere oluşturma
root = tk.Tk()
root.title("계산기프로젝트/CalculatorApp")
root.configure(bg="#FF69B4")

# Giriş kutusu
entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Butonların tanımları
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("x", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("←", 4, 0), ("0", 4, 1), (",", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("√", 5, 1), ("**", 5, 2), ("=", 5, 3)
]

# Butonları arayüze ekleme
for button in buttons:
    text, row, col = button[:3]
    colspan = button[3] if len(button) > 3 else 1

    btn = tk.Button(root, text=text, width=5 * colspan, height=2, font=("Arial", 14),
                    bg="#FF1493", fg="white",
                    relief="ridge", borderwidth=3,
                    command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# Tkinter döngüsü
root.mainloop()
