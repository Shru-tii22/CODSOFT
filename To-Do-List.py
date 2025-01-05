import tkinter as tk
from tkinter import messagebox

class ToDolist:
    def __init__(self,root):
        self.root= root
        self.root.title("To-Do List")
        self.root.geometry('400x400')
        self.root.configure(bg="#e1e6fa")

        
        self.task_entry=tk.Entry(root,font=("arial",12),width=30,bg="#fefefe")
        self.task_entry.place(x=70,y=30)

        
        self.add_button=tk.Button(root,text="Create Task ",bg="#355f2e", fg="white", font=("arial",10),command=self.add_task)
        self.add_button.place(x=50,y=70)
        self.update_button=tk.Button(root,text="Update Task ",bg="#213555", fg="white", font=("arial",10),command=self.update_task)
        self.update_button.place(x=170,y=70)
        self.delete_button=tk.Button(root,text="Delete Task ",bg="#FF0000", fg="white", font=("arial",10),command=self.delete_task)
        self.delete_button.place(x=290,y=70)

        
        self.task_listbox=tk.Listbox(root,bg="#ffffff", font=("arial",12),width=30,height=12, selectmode=tk.SINGLE)
        self.task_listbox.place(x=70,y=120)
        self.tasks=[]

    def add_task(self):
        task=self.task_entry.get()
        if task.strip():
            self.task_listbox.insert(tk.END,task)
            self.tasks.append(task)
            self.task_entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Input Error","Task cannot be Empty")
    
    def update_task(self):
        try:
            selected_index=self.task_listbox.curselection()[0]
            new_task=self.task_entry.get()
            if new_task.strip():
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index,new_task)
                self.tasks[selected_index]=new_task
                self.task_entry.delete(0,tk.END)
              
            else:
                messagebox.showwarning("Input Error","Task cannot be Empty")
        except IndexError:
            messagebox.showwarning("selection error","No task selected to Update")

    def delete_task(self):
        try:
            selected_index=self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Selection Error","No task selected to delete") 
if __name__=="__main__":
    root=tk.Tk()
    app=ToDolist(root)
    root.mainloop() 


