import tkinter as tk
def validate_input(char):
    return char.isdigit()
def on_enter(event):
    current_text = event.widget.get()
    if not validate_input(current_text):
        event.widget.delete(0, tk.END)
root = tk.Tk()
entry = tk.Entry(root, validate = "key", validatecommand = (root.register(validate_input), "%S"))
entry.pack(pady = 10)
entry.bind("<Return>", on_enter)
root.mainloop()