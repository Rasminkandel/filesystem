import tkinter as tk
from tkinter import filedialog, messagebox
import os

class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("rasmin File System")
        self.root.configure(background='#333333', width=500, height=300)

        # Create buttons
        buttons = [
            ("Create File", self.create_file),
            ("List Hidden Files", self.list_hidden_files),
            ("Write to File", self.write_file),
            ("Read File", self.read_file),
            ("Delete File", self.delete_file),
            ("Set Permissions", self.set_permissions),
            ("Exit", self.exit)
        ]

        for btn_text, command in buttons:
            btn = tk.Button(self.root, text=btn_text, command=command, bg='#ffffff', fg='#000000')
            btn.pack(padx=20, pady=5)

    def create_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w'):
                    messagebox.showinfo("Success", f"File '{os.path.basename(file_path)}' created.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def list_hidden_files(self):
        files = os.listdir('.')
        hidden_files = [f for f in files if f.startswith('.')]
        tk.messagebox.showinfo("Hidden Files", '\n'.join(hidden_files))

    def write_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            content = input("Enter the content: ")
            with open(file_path, 'w') as f:
                f.write(content)
            messagebox.showinfo("Success", f"File '{os.path.basename(file_path)}' written.")

    def read_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as f:
                content = f.read()
            messagebox.showinfo("File Content", content)

    def delete_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            os.remove(file_path)
            messagebox.showinfo("Success", f"File '{os.path.basename(file_path)}' deleted.")

    def exit(self):
        self.root.destroy()

    def set_permissions(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            permissions = input("Enter the permissions (e.g. 777): ")
            try:
                os.chmod(file_path, int(permissions, 8))  # Convert permissions to octal
                messagebox.showinfo("Success", f"Permissions for file '{os.path.basename(file_path)}' set to {permissions}.")
            except ValueError:
                messagebox.showinfo("Error", f"Invalid permissions: {permissions}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemGUI(root)
    root.mainloop()
