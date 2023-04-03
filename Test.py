import tkinter as tk

def callback(entry):
    text_utf8 = entry.get().encode("utf-8")
    print(entry)
    print(text_utf8, type(text_utf8))
                         
root = tk.Tk()
entry = tk.Entry(root, width=10)
entry.insert(tk.END, "Hélène")
entry.pack()
button = tk.Button(text="Click me", command=lambda: callback(entry))
button.pack()
root.mainloop()