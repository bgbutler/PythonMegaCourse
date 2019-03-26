
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
from tkinter import ttk
from tkinter import scrolledtext
import backend as bk


window = Tk()
window.title("My Bookstore")


# make the labels Author, Title, Year, ISBN

l1 = ttk.Label(window, text="Title")
l1.grid(row = 0, column = 0)

l2 = ttk.Label(window, text="Author")
l2.grid(row = 0, column = 2)

l3 = ttk.Label(window, text="Year")
l3.grid(row = 1, column = 0)

l4 = ttk.Label(window, text="ISBN")
l4.grid(row = 1, column = 2)

# make the entry boxes
# first make the variables
title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()

# now the boxes
e1 = ttk.Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

e2 = ttk.Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

e3 = ttk.Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

e4 = ttk.Entry(window, textvariable = isbn_text)
e4.grid(row = 0, column = 3)

# need a listbox
# needs a scrollbar to attach to the list1
vert_span = 6

list1 = scrolledtext.ScrolledText(window, height = vert_span, width = 35)
list1.grid(row = 2, column = 0, rowspan = vert_span, columnspan = 2, padx = 20, pady = 40)

# commands for populating the boxes
def view_command():
    list1.delete(END)
    for row in bk.view():
        # ensure that each row is separate
        list1.insert(END, row)


# buttons
b1 = ttk.Button(window, text = "View All", width = 12,command=view_command)
b1.grid(row = 2, column = 3)

b2 = ttk.Button(window, text = "Search entry", width = 12)
b2.grid(row = 3, column = 3)

b3 = ttk.Button(window, text = "Add entry", width = 12)
b3.grid(row = 4, column = 3)

b4 = ttk.Button(window, text = "Update", width = 12)
b4.grid(row = 5, column = 3)

b5 = ttk.Button(window, text = "Delete", width = 12)
b5.grid(row = 6, column = 3)

b6 = ttk.Button(window, text = "Close", width = 12)
b6.grid(row = 7, column = 3)

window.mainloop()
