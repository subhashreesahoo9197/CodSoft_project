import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    name = name_entry.get()
    password_length = int(length_entry.get())
    
    if password_length < 6:
        messagebox.showerror("Not Strong", "Password length should be at least of 6 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
def reset_values():
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator for CodSoft")

def accept_values():
    messagebox.showinfo("Password", "This password is asigned to the user")

frame = tk.Frame(root)
frame.pack(padx=50, pady=50)

name_label = tk.Label(frame, text="ID Name:")
name_label.pack()

name_entry = tk.Entry(frame)
name_entry.pack()

length_label = tk.Label(frame, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(frame)
length_entry.pack()

generate_button = tk.Button(frame, text="->Generate Password-<", command=generate_password)
generate_button.pack()

password_entry = tk.Entry(frame)
password_entry.pack()

reset_button = tk.Button(frame, text="Reset", command=reset_values)
reset_button.pack()

accept_button = tk.Button(frame, text="Accept", command=accept_values)
accept_button.pack()

root.mainloop()