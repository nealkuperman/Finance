# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:46:07 2021

@author: Barry
"""
"""
https://stackoverflow.com/questions/40451300/tkinter-in-spyder
"""
import os
import os.path
import datetime as dt
# import dancis_ttk3
# from tkcalendar import Calendar, DateEntry
from os import path
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog
from dancis_ttk4 import FilePicker
from tkinter.messagebox import showinfo


# date_entry= DateEntry(root)
# date_entry.pack()
# now= date_entry.get()


def quitbtn_clicked():
    root.destroy()

def runbtn_clicked():
    rangebtn_clicked(0)
    valid_files = []
    for x in files:
        if x.filename != "":
            if path.exists(x.filename):
                valid_files.append([x.btn.cget('text'), ":",  x.filename])

    if valid_files:
        showinfo(title="Selected File", message=valid_files)
    else:
        showinfo(title="Selected File", message="No Files Selected")


def create_ttklabel(parent, lbl_txt, row, col):
    label = ttk.Label(parent, text=lbl_txt)
    label.grid(row=row, column=col)
    return label


def create_ttkentry(parent, entry_txt, wdth, row, col):
    entry = ttk.Entry(parent, width=wdth)
    entry.grid(row=row, column=col)
    entry.insert(0, entry_txt)
    return entry


def create_ttklabeledentry(parent, lbl_txt, entry_txt, wdth, row, entrycol, labelcol):
    create_ttklabel(parent, lbl_txt, row, labelcol)
    return create_ttkentry(parent, entry_txt, wdth, row, entrycol)


def create_ttkbutton(parent, btn_lbl, command, row, col):
    button = ttk.Button(parent, text=btn_lbl,
                        command=command)
    button.grid(row=row, column=col)
    return button


def rangebtn_clicked(event):
    if StartYear.get().isnumeric() and endYear.get().isnumeric():
        year_range_value = int(endYear.get())-int(StartYear.get())
        year_range_text = str(year_range_value)
        year_range.configure(text=year_range_text)
        # year_range_lbl.configure(text= "Range =")
    else:
        print("Failed")

root = Tk()
root.title("Sum Calculator")
root.geometry('600x300')
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

quitbtn = create_ttkbutton(root, "Quit", quitbtn_clicked, 11, 4)

runbtn = create_ttkbutton(root, "Run", runbtn_clicked, 10, 4)


# Init loc variables
labelcol = 0
entrycol = labelcol + 1
nextrow = 0
PATH_ENTRY_WIDTH = 40

StartYear = create_ttklabeledentry(root, "Starting Year", "1994", 4, nextrow, entrycol, labelcol)
StartYear.bind("<KeyRelease>", rangebtn_clicked)
nextrow += 1
endYear = create_ttklabeledentry(root, "Ending Year", str(dt.datetime.now().year), 4, nextrow, entrycol, labelcol)
endYear.bind("<KeyRelease>", rangebtn_clicked)
nextrow += 1
year_range_lbl = create_ttklabel(root, "Year Range:", nextrow, labelcol)
year_range = create_ttklabel(root, "", nextrow, entrycol)
year_range.configure(text=int(endYear.get())-int(StartYear.get()))
nextrow += 1
stockSource = create_ttklabeledentry(root, "Stock Source", "Yahoo", 10, nextrow, entrycol, labelcol)
nextrow += 1
stockName = create_ttklabeledentry(root, "Stock Name", "NFLX", 10, nextrow, entrycol, labelcol)
nextrow += 1
startDatelbl = create_ttklabel(root, "Start Date", nextrow, labelcol)
# .pack(padx=10, pady=10)

# nextrow += 1
# rangebtn = create_ttkbutton(root, "Calc Range", rangebtn_clicked(0), nextrow, 0)

today = dt.date.today()

mindate = dt.date(year=1944, month=6, day=11)
maxdate = today
print(mindate, maxdate)

StartDate = DateEntry(root, width=11, \
                            background='darkblue', \
                            foreground='white', \
                            borderwidth=2, \
                            mindate=mindate,
                            maxdate=maxdate,
                            date_pattern='MM/dd/yyyy',
                            day=mindate.day,
                            month=mindate.month,
                            year=mindate.year)
StartDate.grid(row=5, column=1)
# StartDate.pack(padx=10, pady=10)

files = []
nextrow += 1
watchlist_file_picker = FilePicker(root, "Watchlist", PATH_ENTRY_WIDTH, labelcol, entrycol, nextrow)
files.append(watchlist_file_picker)
nextrow += 1
portfolio_file_picker = FilePicker(root, "Portfolio", PATH_ENTRY_WIDTH, labelcol, entrycol, nextrow)
files.append(portfolio_file_picker)
nextrow += 1
allocation_file_picker = FilePicker(root, "Allocation", PATH_ENTRY_WIDTH, labelcol, entrycol, nextrow)
files.append(allocation_file_picker)

root.mainloop()
