# This script was contributed to the curriculum by Albert Haskie, GitHub@BirdMan721

import random
import tkinter as tk
from tkinter import messagebox
import os

class NameGroupRandomizer:
    def __init__(self, names):
        self.names = names

    def create_groups(self, group_size):
        random.shuffle(self.names)
        groups = [self.names[i:i + group_size] for i in range(0, len(self.names), group_size)]
        return groups

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Name Group Randomizer")
        self.geometry("400x600")

        self.names = self.load_names_from_file()
        self.groups = self.load_groups_from_file()

        self.label = tk.Label(self, text="Enter names one by one:")
        self.label.pack(pady=10)

        self.entry_name = tk.Entry(self, width=30)
        self.entry_name.pack(pady=10)

        self.add_button = tk.Button(self, text="Add Name", command=self.add_name)
        self.add_button.pack(pady=5)

        self.names_listbox = tk.Listbox(self)
        self.names_listbox.pack(pady=10)
        self.update_listbox()

        self.delete_button = tk.Button(self, text="Delete Selected Name", command=self.delete_name)
        self.delete_button.pack(pady=5)

        self.label_group_size = tk.Label(self, text="Enter group size:")
        self.label_group_size.pack(pady=10)

        self.entry_group_size = tk.Entry(self, width=10)
        self.entry_group_size.pack(pady=10)

        self.create_groups_button = tk.Button(self, text="Create Groups", command=self.create_groups)
        self.create_groups_button.pack(pady=20)

        self.show_groups_button = tk.Button(self, text="Show Last Groups", command=self.show_groups)
        self.show_groups_button.pack(pady=10)

    def add_name(self):
        name = self.entry_name.get()
        if name:
            self.names.append(name)
            self.update_listbox()
            self.entry_name.delete(0, tk.END)
            self.save_names_to_file()

    def delete_name(self):
        selected_index = self.names_listbox.curselection()
        if selected_index:
            self.names.pop(selected_index[0])
            self.update_listbox()
            self.save_names_to_file()

    def update_listbox(self):
        self.names_listbox.delete(0, tk.END)
        for name in self.names:
            self.names_listbox.insert(tk.END, name)

    def save_names_to_file(self):
        folder_path = "name_group_data"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, "names.txt")
        with open(file_path, "w") as file:
            for name in self.names:
                file.write(f"{name}\n")

    def load_names_from_file(self):
        folder_path = "name_group_data"
        file_path = os.path.join(folder_path, "names.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                names = file.read().splitlines()
            return names
        return []

    def save_groups_to_file(self, groups):
        folder_path = "name_group_data"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, "groups.txt")
        with open(file_path, "w") as file:
            for i, group in enumerate(groups):
                file.write(f"Group {i+1}: {', '.join(group)}\n")

    def load_groups_from_file(self):
        folder_path = "name_group_data"
        file_path = os.path.join(folder_path, "groups.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                groups = file.read().splitlines()
            return groups
        return []

    def create_groups(self):
        try:
            group_size = int(self.entry_group_size.get())
            if group_size <= 0:
                raise ValueError("Group size must be a positive integer.")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
            return

        if not self.names:
            messagebox.showerror("No names", "Please add some names first.")
            return

        randomizer = NameGroupRandomizer(self.names)
        groups = randomizer.create_groups(group_size)
        self.save_groups_to_file(groups)

        group_text = ""
        for i, group in enumerate(groups):
            group_text += f"Group {i+1}: {', '.join(group)}\n"

        messagebox.showinfo("Groups", group_text)

    def show_groups(self):
        if not self.groups:
            messagebox.showinfo("No groups", "No groups to display.")
            return

        group_text = "\n".join(self.groups)
        messagebox.showinfo("Last Groups", group_text)

if __name__ == "__main__":
    app = Application()
    app.mainloop()


