import tkinter as tk

def button_click(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying input and results
entry = tk.Entry(root, width=16, font=('Arial', 20), bd=5, insertwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place the buttons on the grid
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=4, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Additional buttons
tk.Button(root, text='C', width=4, height=2, command=button_clear).grid(row=row_val, column=col_val)
tk.Button(root, text='=', width=4, height=2, command=button_equal).grid(row=row_val, column=col_val + 1)

# Start the Tkinter event loop
root.mainloop()
