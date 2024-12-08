import tkinter as tk
root = tk.Tk()
def Insert(event : "tk.Event") -> None :
    btn_type = event.widget.cget("text")
    if Output.get() == " Error" : Clear_Content()
    match btn_type :
        case "(" : Output.insert(tk.END, " (")
        case ")" : Output.insert(tk.END, ") ")
        case "÷" : Output.insert(tk.END, " ÷ ")
        case "×" : Output.insert(tk.END, " × ")
        case "-" : Output.insert(tk.END, " - ")
        case "+" : Output.insert(tk.END, " + ")
        case _ : Output.insert(tk.END, str(btn_type))
def Clear_Content() -> None :
    Output.delete(0, tk.END) ; Output.insert(tk.END, " ")
def Calculate() -> None :
    Storage : str = Output.get() ; Storage = Storage.replace("×", "*") ; Storage = Storage.replace("÷", "/") ; Storage = Storage.replace("%", "/100")
    if Storage in [" ", ""] : return
    try :
        Result = eval(Storage)
        if Result % 1 == 0 : Result = f"{Result:.0f}"
        Clear_Content() ; Output.insert(tk.END, str(Result))
    except Exception as E :
        Clear_Content() ; Output.insert(tk.END, "Error")
root.geometry("340x500") ; root.title("Calculator") ; root.resizable(False, False) ; root.config(bg= "gray10")
for i in range(0,7) :
    root.rowconfigure(index = i, weight = 1)
    if i in range(0, 4) : root.columnconfigure(index = i, weight = 1)
Output = tk.Entry(master = root, font = ("Xenara", 35), background = "gray12", foreground = "white", width = 330, borderwidth = 0) ; Output.grid(row = 0, column = 0, columnspan = 4, rowspan = 2, padx = 5, pady = (10, 5), sticky = "ns")
button_types : dict = {"Left_Parenthesis" : "(","Right_Parenthesis" : ")","Percentage" : "%","Clear" : "AC","Int_7" : "7","Int_8" : "8","Int_9" : "9","Divide" : "÷","Int_4" : "4","Int_5" : "5","Int_6" : "6","Multiply" : "×","Int_1" : "1","Int_2" : "2","Int_3" : "3","Subtraction" : "-","Int_0" : "0","Decimal" : ".","Calculate_btn" : "=","Addition" : "+"}
i_row : int = 2 ; i_col : int = 0
for item in button_types :
    item = tk.Button(master = root, text = button_types[item], font = ("Xenara", 25), width = 65, height = 1, background = "gray12", foreground = "white", borderwidth = 0) ; item.grid(row = i_row, column = i_col, padx = 5, pady = 5)
    if (i_row == 2) and (i_col == 3) : item.bind("<Button-1>", lambda event : Clear_Content())
    elif (i_row == 6) and (i_col == 2) : item.bind("<Button-1>", lambda event : Calculate())
    else : item.bind("<Button-1>", Insert)
    i_col += 1
    if i_col > 3 : i_col = 0 ; i_row += 1
root.bind("<Return>", lambda event : Calculate())
root.mainloop()

# just disables alpha or symbolic inputs, test.py as example
# %S for key checks, %V for key stroke actions only?
# yet to be covered
# Output = tk.Entry(master = root, font = ("Xenara", 35), background = "gray12", foreground = "white", width = 330, borderwidth = 0, validate = "key", validatecommand = (root.register(Val_Entry), "%S"))
"""def Val_Entry(character : str) -> None :
    print(character)
    return (character.isdigit()) or (character in ["/", "*", "+", "-", "%", "AC", "(", ")"])"""