import datetime as dt
from os import path
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from label_ttk import LabeledFilePicker, LabeledDateEntry, LabeledEntry, LabeledLabel, create_ttkbutton, \
    create_ttkentry, create_ttklabel
from tkinter.messagebox import showinfo

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:46:07 2021

@author: Barry
"""
"""
https://stackoverflow.com/questions/40451300/tkinter-in-spyder
"""


# date_entry= DateEntry(root)
# date_entry.pack()
# now= date_entry.get()


def quitbtn_clicked():
    root.destroy()


def runbtn_clicked():
    valid_files = []
    invalid_files = []
    no_files = []
    for x in files:
        print(x.button.cget('text'), x.filename)
        if x.filename != "":
            if path.exists(x.filename):
                valid_files.append("".join([x.button.cget('text'), ": ",  x.filename]))
            else:
                invalid_files.append("".join([x.button.cget('text'), ": ",  x.filename]))
        else:
            no_files.append("".join([x.button.cget('text'), ": ", x.NO_FILE_TEXT]))

    filestatus = []
    if valid_files:
        filestatus.append("Valid_Files: ")------
        filestatus += valid_files
    if invalid_files:
        filestatus.append("Invalid Files: ")
        filestatus += invalid_files
    if no_files:
        filestatus.append("Missing Files: ")
        filestatus += no_files
    showinfo(title="Selected File", message='\n'.join(filestatus))


def rangebtn_clicked(event):
    if StartYear.entry.get().isnumeric() and endYear.entry.get().isnumeric():
        year_range_value = int(endYear.entry.get())-int(StartYear.entry.get())
        year_range_text = str(year_range_value)
        year_range.label2.configure(text=year_range_text)
    else:
        print("Failed")


root = Tk()
root.title("Sum Calculator")
root.geometry('600x300')
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes, '-topmost', False)

quitbtn = create_ttkbutton(root, "Quit", quitbtn_clicked, 11, 4)

runbtn = create_ttkbutton(root, "Run", runbtn_clicked, 10, 4)


# Init loc variables
labelcol = 0
entrycol = labelcol + 1
nextrow = 0
PATH_ENTRY_WIDTH = 40

StartYear = LabeledEntry(root, "Starting Year", labelcol, "1994", entrycol, 4, nextrow, True)
StartYear.entry.bind("<KeyRelease>", rangebtn_clicked)

nextrow += 1
endYear = LabeledEntry(root, "Ending Year", labelcol, str(dt.datetime.now().year), entrycol, 4, nextrow, True)
endYear.entry.bind("<KeyRelease>", rangebtn_clicked)

nextrow += 1
year_range = LabeledLabel(root, "Year Range:", labelcol, int(endYear.entry.get())-int(StartYear.entry.get()), entrycol, nextrow)

nextrow += 1
stockSource = LabeledEntry(root, "Stock Source", labelcol, "Yahoo", entrycol, 10, nextrow, True)

nextrow += 1
stockName = LabeledEntry(root, "Stock Name", labelcol, "NFLX", entrycol, 10, nextrow, True)

nextrow += 1
today = dt.date.today()
StartDate_mindate = dt.date(year=1944, month=6, day=11)
StartDate_maxdate = today
StartDate = LabeledDateEntry(root, StartDate_mindate, StartDate_maxdate, StartDate_mindate, "Start Date", nextrow, labelcol, entrycol)

files = []

nextrow += 1
watchlist_file_picker = LabeledFilePicker(root, "Watchlist", PATH_ENTRY_WIDTH, labelcol, entrycol, nextrow)
files.append(watchlist_file_picker)

nextrow += 1
portfolio_file_picker = LabeledFilePicker(root, "Portfolio", PATH_ENTRY_WIDTH, labelcol, entrycol, nextrow)
files.append(portfolio_file_picker)

nextrow += 1
allocation_file_picker = LabeledFilePicker(root, "Allocation", PATH_ENTRY_WIDTH, labelcol, entrycol, nextrow)
files.append(allocation_file_picker)

root.mainloop()
