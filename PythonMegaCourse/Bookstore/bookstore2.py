
# program to to access a database
# uses a GUI to take the input
"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an Entry
Add Entry
Update Entry
Delete
Close

"""
# best to use a grid to set up the GUI
from tkinter import *
# from tkinter import ttk
# from tkinter import scrolledtext
import backend as bk


# commands for populating the boxes
def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0, END)
    for row in bk.view():
        # ensure that each row is separate
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in bk.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    bk.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    bk.delete(selected_tuple[0])

def update_command():
    bk.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    print(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])



window = Tk()
window.title("My Bookstore")


# make the labels Author, Title, Year, ISBN
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text="Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text="Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text="ISBN")
l4.grid(row = 1, column = 2)

# make the entry boxes
# first make the variables
title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()

# now the boxes
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

# need a listbox
# needs a scrollbar to attach to the list1
vert_span = 6

sb1 = Scrollbar(window)
sb1.grid(row = 2, columns = 2, rowspan = 6)

list1 = Listbox(window, height = vert_span, width = 35)
list1.grid(row = 2, column = 0, rowspan = vert_span, columnspan = 2, padx = 20, pady = 40)

list1.configure(yscrollcommand=sb1.set)
sb1.grid(row = 2, column = 0, rowspan = vert_span)

list1.bind('<<ListboxSelect>>', get_selected_row)



# buttons
b1 = Button(window, text = "View All", width = 12,command=view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command=search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command=add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update", width = 12, command=update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete", width = 12, command=delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command=window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()
