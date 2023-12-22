# Import the required Package for TO-DO-LIST
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

# Function to add the task
def add_task():
    task_string = task_feild.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty')  # Corrected the typo "Feild" to "Field"
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values(?)', (task_string,))
        list_update()
        task_feild.delete(0, 'end')

# Function to Update any task
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

# Function to delete any Task
def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No task selected. Cannot Delete.')

# Function to delete All task
def delete_all_task():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  # Corrected the space after 'Delete All'
    if message_box == True:
        while (len(tasks) != 0):
            tasks.pop()
        the_cursor.execute('Delete from tasks')
        list_update()

# Function to Clear All the list
def clear_list():
    task_listbox.delete(0, 'end')  # Corrected 'End' to 'end'

# Function to close the window
def close():
    print(tasks)
    guiWindow.destroy()

# Function to retrive the database
def retrieve_database():  # Corrected the function name 'retrive_database' to 'retrieve_database'
    while (len(tasks) != 0):
        tasks.pop()
    for row in the_cursor.execute('Select title from tasks'):  # Corrected 'task' to 'tasks'
        tasks.append(row[0])

# This function defines all the task to be used in a TO-DO-LIST
if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do-List(75-Days)")
    guiWindow.geometry("665x400+550+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#B3E5CF")

    the_connection = sql.connect('listofTasks.db')
    the_cursor = the_connection.cursor()
    # Corrected the SQL query
    the_cursor.execute('create table if not exists tasks(title text)')

    tasks = []

    function_frame = Frame(guiWindow, bg="#8EE5EE")

    function_frame.pack(side="top", expand=True, fill="both")

    task_label = Label(function_frame, text="TO-DO-LIST \n Enter the task title:", font=("arial", "14", "bold"),
                       background="#8EE5EE", foreground="#FF6103")
    task_label.place(x=20, y=30)

    task_feild = Entry(function_frame, font=("Arial", "14"), width=42, background="white", foreground="black")
    task_feild.place(x=180, y=30)

    # Commands to perform functions like add,delete,deleteall,exit.....
    add_button = Button(function_frame, text="Add", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=add_task)
    del_button = Button(function_frame, text="Remove", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=delete_task)
    del_all_button = Button(function_frame, text="Delete All", width=15, bg='#D4AC0D', font=("arial", "14", "bold"),command=delete_all_task)
    exit_button = Button(function_frame, text="Exit", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=close)

    # Commands to place Buttons like add,delete,deleteall,exit....
    add_button.place(x=18, y=80)
    del_button.place(x=240, y=80)
    del_all_button.place(x=460, y=80)
    exit_button.place(x=17, y=330)

    task_listbox = Listbox(function_frame, width=70, height=9, font="bold", selectmode="SINGLE", background="WHITE",
                           foreground="BLACK", selectbackground="#FF8C00", selectforeground="BLACK")
    task_listbox.place(x=17, y=140)

    # Corrected the function name 'retrive_database' to 'retrieve_database'
    retrieve_database()  
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
