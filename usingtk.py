import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        # Initialize the ToDoApp with a Tkinter root window
        self.root = root
        self.root.title("To-Do List App")  # Set the title of the window
        self.root.geometry("400x400")  # Set the initial size of the window

        self.tasks = []  # List to store tasks

        # Entry widget for entering tasks
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=20)  # Add padding between the entry widget and other components

        # Button to add tasks
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        # Button to remove selected task
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        # Define the action when the window close button is clicked
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        # Function to add a task to the listbox
        task = self.task_entry.get()  # Get the task from the entry widget
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)  # Insert the task into the listbox
            self.task_entry.delete(0, tk.END)  # Clear the entry widget after adding the task
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        # Function to remove a selected task from the listbox
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
            messagebox.showinfo("Task Removed", f"Task '{task}' removed successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def on_closing(self):
        # Function to handle the window close button
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
