import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("C:\\Python Project\\tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)


def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("C:\\Python Project\\tasklist.txt",'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        listbox.delete( ANCHOR)



def openTaskfile():
        
        try:
            global task_list
        
            with open("C:\\Python Project\\tasklist.txt","r") as taskfile:
              task = taskfile.readlines()
        
            for task in task:
              if task !="\n":
                   task_list.append(task)
                   listbox.insert(END ,task)
        except:
            file=open('C:\\Python Project\\tasklist.txt','w')
            file.close()

#icon
Image_icon=PhotoImage(file="C:\\Python Project\Foto\\task.png")
root.iconphoto(False,Image_icon)

#top bar
TopImage=PhotoImage(file="C:\\Python Project\Foto\\topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="C:\\Python Project\\Foto\\dock.png")
Label(root,image=dockImage,bg="black").place(x=30,y=30)

noteImage=PhotoImage(file="C:\\Python Project\\Foto\\task.png")
Label(root,image=noteImage,bg="black").place(x=325,y=25)

heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="black")
heading.place(x=120,y=25)

#main
frame= Frame(root,width=400,height=22,bg="white")
frame.place(x=0,y=180)


task=StringVar()
task_entry=Entry(root,width=35,font="arial 20",bd=0)
task_entry.place(x=0,y=150)
task_entry.focus()

button=Button(root,text="ADD",font="arial 20 bold",width=6,bg="light blue",fg="white",bd=0,command=addTask)
button.place(x=300,y=150)

#listbox
frame1= Frame(root,bd=3,width=700,height=280,bg="gray")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font="arial 12",width=40,height=16,bg="pink",fg="black",cursor="hand2",selectbackground="light blue")
listbox.pack(side=LEFT , fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT , fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskfile()

#delete
Delete_icon=PhotoImage(file="C:\\Python Project\\Foto\\delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

root.mainloop()
