from tkinter import *

def deleteTask(task):
    task = task + "\n"
    try:
        with open("tasks.txt", "r") as f:
            tasksList = f.readlines()
        
        if task in tasksList:
            tasksList.remove(task)
            with open("tasks.txt", "w") as f:
                f.writelines(tasksList)
        
        refreshTasks()
    except FileNotFoundError:
        pass

def addTaskButton():
    task = task_input.get().strip()
    if task:
        with open("tasks.txt", "a") as f:
            f.write(f"{task}\n")
        task_input.delete(0, END) 
        refreshTasks() 

def clearTaskDisplay():
    for widget in task_frame.winfo_children():
        widget.destroy()

def getTasks():
    clearTaskDisplay()
    try:
        with open("tasks.txt", "r") as f:
            tasksList = f.readlines()
            for t in tasksList:
                t = t.strip() 
                if t:  
                    task_item_frame = Frame(task_frame)
                    task_item_frame.pack(fill=X, padx=5, pady=2)
                    
                    task_L_label = Label(task_item_frame, text=t, anchor="w")
                    task_L_label.pack(side=LEFT, fill=X, expand=True)
                    
                    delete_btn = Button(task_item_frame, text="Delete", 
                                      command=lambda task=t: deleteTask(task))
                    delete_btn.pack(side=RIGHT)
    except FileNotFoundError:
        open("tasks.txt", "w").close()

def refreshTasks():
    getTasks()

window = Tk()
window.title("ToDoList App")
window.geometry("400x500")

title_label = Label(text="ToDoList App", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Input section
input_frame = Frame(window)
input_frame.pack(pady=10)

task_label = Label(input_frame, text="Enter Task Here:")
task_label.pack()

task_input = Entry(input_frame, width=30)
task_input.pack(pady=5)

task_add_btn = Button(input_frame, text="ADD", font=("Arial", 12, "bold"), 
                     command=addTaskButton)
task_add_btn.pack(pady=5)

# Display section
display_frame = Frame(window)
display_frame.pack(pady=10)


# Tasks display area
task_frame = Frame(window)
task_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Load tasks on startup
getTasks()

window.mainloop()