import tkinter as tk
from tkinter import messagebox
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo App")

        self.console = Console()

        # Styling
        self.configure(bg="#F5F5F5")
        self.label_font = ("Arial", 12, "bold")
        self.entry_font = ("Arial", 10)
        self.button_font = ("Arial", 10, "bold")
        self.text_font = ("Arial", 10)

        # Text Entry
        self.task_entry = tk.Entry(self, width=40, font=self.entry_font)
        self.task_entry.grid(row=0, column=0, pady=10, padx=10)

        self.category_entry = tk.Entry(self, width=40, font=self.entry_font)
        self.category_entry.grid(row=1, column=0, pady=10, padx=10)

        # Buttons
        add_button = tk.Button(self, text="Add Todo", command=self.add_todo, font=self.button_font, bg="#4CAF50", fg="white")
        add_button.grid(row=2, column=0, pady=10, padx=10)

        delete_button = tk.Button(self, text="Delete Todo", command=self.delete_todo, font=self.button_font, bg="#FF5733", fg="white")
        delete_button.grid(row=3, column=0, pady=10, padx=10)

        update_button = tk.Button(self, text="Update Todo", command=self.update_todo, font=self.button_font, bg="#3498DB", fg="white")
        update_button.grid(row=4, column=0, pady=10, padx=10)

        complete_button = tk.Button(self, text="Complete Todo", command=self.complete_todo, font=self.button_font, bg="#9B59B6", fg="white")
        complete_button.grid(row=5, column=0, pady=10, padx=10)

        show_button = tk.Button(self, text="Show Todos", command=self.show_todos, font=self.button_font, bg="#34495E", fg="white")
        show_button.grid(row=6, column=0, pady=10, padx=10)

        # Text widget for displaying todos
        self.todo_text = tk.Text(self, wrap="word", width=40, height=20, font=self.text_font, bg="#ECF0F1")
        self.todo_text.grid(row=0, column=1, rowspan=7, padx=10, pady=10)

    def add_todo(self):
        task = self.task_entry.get()
        category = self.category_entry.get()
        todo = Todo(task, category)
        insert_todo(todo)
        self.show_todos()

    def delete_todo(self):
        try:
            position = int(self.task_entry.get())
            delete_todo(position-1)
            self.show_todos()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid position")

    def update_todo(self):
        try:
            position = int(self.task_entry.get())
            task = self.category_entry.get()
            update_todo(position-1, task, None)
            self.show_todos()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid position")

    def complete_todo(self):
        try:
            position = int(self.task_entry.get())
            complete_todo(position-1)
            self.show_todos()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid position")

    def show_todos(self):
        tasks = get_all_todos()
        self.console.print("[bold magenta]Todos[/bold magenta]!", "💻")

        self.todo_text.delete(1.0, tk.END)  # Clear the text widget

        def get_category_color(category):
            COLORS = {'Learn': '#3498DB', 'YouTube': '#E74C3C', 'Sports': '#2ECC71', 'Study': '#F39C12'}
            if category in COLORS:
                return COLORS[category]
            return '#BDC3C7'

        for idx, task in enumerate(tasks, start=1):
            c = get_category_color(task.category)
            is_done_str = '✅' if task.status == 2 else '❌'
            todo_str = f"{idx}. {task.task} - {task.category} - {is_done_str}\n"
            self.todo_text.insert(tk.END, todo_str)

if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.mainloop()
