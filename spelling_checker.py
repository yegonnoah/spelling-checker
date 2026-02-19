import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.config(bg="#dae6f6")
root.geometry("700x400")

def check_spelling():
    word=entry.get()
    check=TextBlob(word)
    right=str(check.correct())

    cs=Label(root,text="Correct text is :",font="poppins 14",bg="#dae6f6",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)

##icon
icon=PhotoImage(file="s2.png")
root.iconphoto(False,icon)


title=Label(root,text="Spelling Checker",font=("Trebuchet MS",20,"bold"),bg="#dae6f6",fg="#364971")
title.pack(pady=(50,0))

entry=Entry(root,justify="center",width=30,font="poppins 25",bg="white",border=2)
entry.pack(pady=10)
entry.focus()

button=Button(root,text="Check",font="arial 14 bold",bg="#364971",fg="white",cursor="hand2",command=check_spelling)
button.pack()

spell=Label(root,font="poppins 14 italic",bg="#dae6f6",fg="#364971")
spell.place(x=250,y=250)


root.mainloop()