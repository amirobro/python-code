from tkinter import *
import tkinter.ttk as ttk
from model.db.persondb import *
import tkinter.messagebox as msg
from cotrooler.person_cotroller import *


def reset_form():
    name.set("")
    family.set("")
    national_id.set("")

    # table clean
    for i in table.get_children():
        table.delete(i)

    # insert   to     table
    for person in find_all():
        table.insert("", END, values=person)


def table_clik(event):
    index = table.focus()
    item = table.item(index)
    person = item['values']
    id.set(person[0])
    name.set(person[1])
    family.set(person[2])
    national_id.set(person[3])


def save_click():
    status, data = save(name.get(), family.get(), national_id.get())
    if status:
        msg.showinfo("Save", data)
        reset_form()
    else:
        msg.showerror("Save Error", data)


def edit_click():
    status, data = edit(id.get(), name.get(), family.get(), national_id.get())
    if status:
        msg.showinfo("Edit", "person edited")
        reset_form()
    else:
        msg.showerror("Edit Error", data)


def remove_click():
    if msg.askyesno("Remove", "are u sure?"):

        status, data = remove(id.get())
        if status:
         msg.showinfo("remove", data)
         reset_form()
        else:
            msg.showerror('remove,Error', data)


win = Tk()
win.title('Person info')
win.geometry("800x600")

# id
id = IntVar()
Label(win, text="ID").place(x=20, y=20)
Entry(win, textvariable=id, state="readonly").place(x=90, y=20)

# Name
name = StringVar()
Label(win, text="name").place(x=20, y=60)
Entry(win, textvariable=name).place(x=90, y=60)

# family
family = StringVar()
Label(win, text="family").place(x=20, y=100)
Entry(win, textvariable=family).place(x=90, y=100)

# national ID
national_id = StringVar()
Label(win, text="National ID").place(x=20, y=140)
Entry(win, textvariable=national_id).place(x=90, y=140)

table = ttk.Treeview(win, columns=(1, 2, 3, 4), show="headings")
table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)

table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="family")
table.heading(4, text="National ID")

table.bind("<ButtonRelease>", table_clik)
table.bind("<KeyRelease>", table_clik)

table.place(x=300, y=20)

Button(win, text="save", command=save_click, width=12).place(x=90, y=259)
Button(win, text="edit", command=edit_click, width=12).place(x=190, y=259)
Button(win, text="remove", command=remove_click, width=12).place(x=290, y=259)

reset_form()

win.mainloop()
