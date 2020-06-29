'''
A grahical user interface program that allows for insertion, modification of data
'''
# importing necessary modules
from tkinter import *
import album_db_backend

def view_command():
    # delete everytime the show album button is clicked
    lst1.delete(0, END)
    for row in album_db_backend.view_data():
        lst1.insert(END,row)
def search_command():
    lst1.delete(0, END)
    #interate through the backend list
    for row in album_db_backend.search_database(title_entry.get(), artist_entry.get(), year_entry.get(), record_label_team.get()):
        lst1.insert(END, row)
def add_command():
    album_db_backend.insert_data(title_entry.get(), artist_entry.get(), year_entry.get(), record_label_team.get())
    lst1.delete(0, END)
    lst1.insert(END, (title_entry.get(), artist_entry.get(), year_entry.get(), record_label_team.get()))
# a parameter is passed inside beause it has been binded called event
def get_selected_row(event):
    global selected_tuple
    row_index = lst1.curselection()[0]
    # get the selected data
    selected_tuple = lst1.get(row_index)

def delete_command():
    album_db_backend.delete(selected_tuple[0])
    view_command()

root = Tk()

lable0 = Label(root, text="Album Database System").grid(row=0, column=1, columnspan=3) #grid your objects properly

lable1 = Label(root, text="Title: ").grid(row=2, column=1) #grid your objects properly
lable2 = Label(root, text="Artist: ").grid(row=2, column=3)
lable3 = Label(root, text="Release Year: ").grid(row=3, column=1)
lable4 = Label(root, text="Record Label: ").grid(row=3, column=3)

# what the user will enter = textvariable
# user entry boxes
title_entry = StringVar()
entry1 = Entry(root, textvariable=title_entry).grid(row=2, column=2)

artist_entry = StringVar()
entry2 = Entry(root, textvariable=artist_entry).grid(row=2, column=4)

year_entry = StringVar()
entry3 = Entry(root, textvariable=year_entry).grid(row=3, column=2)

record_label_team = StringVar()
entry4 = Entry(root, textvariable=record_label_team).grid(row=3, column=4)


# display of our data information box
lable5 = Label(root, text="Output Result: ").grid(row=6, column=0)

lst1 = Listbox(root, height=12, width=40)
lst1_grid = lst1.grid(row=4, column=1, rowspan=6, columnspan=2)
# creating a scrollbar for our listbox object
sb1 = Scrollbar(root)
sb1_grid = sb1.grid(row=4, column=3, rowspan=6)
lst1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lst1.yview)
lst1.bind("<<ListboxSelect>>", get_selected_row)

#Our window buttons
#Display the data in database
bttn1 = Button(root, text="Show Albums", width=11, height=2, command=view_command).grid(row=4, column=4)
#Search for a certain album giving inputs
bttn2 = Button(root, text="Search", width=11, height=2, command=search_command).grid(row=5, column=4)
bttn3 = Button(root, text="Insert Data", width=11, height=2, command=add_command).grid(row=6, column=4)
bttn4 = Button(root, text="Modify", width=11, height=2).grid(row=7, column=4)
bttn5 = Button(root, text="Delete", width=11, height=2,command=delete_command).grid(row=8, column=4)
bttn6 = Button(root, text="Close Window", width=11, height=2, command=root.destroy).grid(row=9, column=4)

#title of the page
root.title("Album Database System")
#changing the size of the window
root.geometry("700x400")
root.resizable(width=TRUE, height=TRUE)

root.mainloop()
