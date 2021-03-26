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
import dancis_ttk3
# from tkcalendar import Calendar, DateEntry
from os import path
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog



# date_entry= DateEntry(root)
# date_entry.pack()
# now= date_entry.get()


def quitbtn_clicked():
    root.destroy()

'''
def runbtn_clicked():
    rangebtn_clicked()
    for lbl in files:
        entry = files.get(lbl)
        # if lbl.cget("text") != 'No File Selected':
        print(lbl.cget("text"))
        if path.exists(entry.get()):
            lbl.config(text=os.path.basename(entry.get()))

        else:
            lbl.config(text=os.path.basename("Invalid File"))
        # watchlist_lbl.config(text=os.path.basename(watchlist_entry.get()))
        # portfolio_lbl.config(text=os.path.basename(portfolio_entry.get()))
        # allocation_lbl.config(text=os.path.basename(allocation_entry.get()))
'''

def create_ttklabel(parent, lbl_txt, row, col):
    label = ttk.Label(parent, text=lbl_txt)
    label.grid(row=row, column=col)
    return label


def create_ttkentry(parent, entry_txt, wdth, row, col):
    entry = ttk.Entry(parent, width=wdth)
    entry.grid(row=row, column=col)
    entry.insert(0, entry_txt)
    # entry.set(entry_txt)
    return entry


def create_ttklabeledentry(parent, lbl_txt, entry_txt, wdth, row, entrycol, labelcol):
    create_ttklabel(parent, lbl_txt, row, labelcol)
    return create_ttkentry(parent, entry_txt, wdth, row, entrycol)


def rangebtn_clicked():
    year_range_value = int(endYear.get())- int(StartYear.get())
    year_range_text = str(year_range_value)
    year_range.configure(text=year_range_text)
    # year_range_lbl.configure(text= "Range =")


def browseFiles(file_control):
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Python files",
                                                      "*.py*"),
                                                     ("all files",
                                                      "*.*")))
    if filename != '':
        file_control.delete(0, END)
        file_control.insert(0, filename)


def create_file_picker(btn_lbl, command, labelcol, nextrow):
    file_picker_btn = ttk.Button(root,
                            text=btn_lbl,
                            command=command)
    file_picker_entry = create_ttkentry(root, "No File Selected", PATH_ENTRY_WIDTH, nextrow, entrycol)
    file_picker_btn.grid(column=labelcol, row=nextrow)
    return file_picker_entry, file_picker_btn


def watchListBtn_Click():
    browseFiles(watchlist_entry)


def portfolioBtn_Click():
    browseFiles(portfolio_entry)


def allocationBtn_Click():
    browseFiles(allocation_entry)


root = Tk()
root.title("Sum Calculator")
root.geometry('600x300')
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

quitbtn = ttk.Button(root, text="Quit",
                       command=quitbtn_clicked)
quitbtn.grid(row=11,column=4)

'''
runbtn = ttk.Button(root, text="Run",
                       command=runbtn_clicked)
runbtn.grid(row=10,column=4)
'''

# Init loc variables
labelcol = 0
entrycol = labelcol + 1
nextrow = 0
PATH_ENTRY_WIDTH = 40

year_range_lbl = create_ttklabel(root, "Year Range:", nextrow, labelcol)
year_range = create_ttklabel(root, "", nextrow, entrycol)
nextrow += 1
StartYear = create_ttklabeledentry(root, "Starting Year", "1994", 4, nextrow, entrycol, labelcol)
nextrow += 1
endYear = create_ttklabeledentry(root, "Ending Year", str(dt.datetime.now().date())[0:4], 4, nextrow, entrycol, labelcol)
nextrow += 1
stockSource = create_ttklabeledentry(root, "Stock Source", "Yahoo", 10, nextrow, entrycol, labelcol)
nextrow += 1
stockName = create_ttklabeledentry(root, "Stock Name", "NFLX", 10, nextrow, entrycol, labelcol)
nextrow += 1
startDatelbl = create_ttklabel(root, "Start date", nextrow, labelcol)
# .pack(padx=10, pady=10)

nextrow += 1
rangebtn = ttk.Button(root, text="Calc Range", \
                  command=rangebtn_clicked)
rangebtn.grid(row=nextrow,column=0)


today = dt.date.today()

mindate = dt.date(year=44, month=6, day=11)
maxdate = today
print(mindate, maxdate)

StartDate = DateEntry(root, width=11, \
                            background='darkblue', \
                            foreground='white', \
                            borderwidth=2, \
                            mindate=mindate,
                            maxdate=maxdate,\
                            year=1944)
StartDate.grid(row=5, column=1)
# StartDate.pack(padx=10, pady=10)
files = {}
nextrow += 1
(watchlist_entry, watchlist_btn) = create_file_picker("Watchlist", watchListBtn_Click, labelcol, nextrow)
files.update({watchlist_btn.cget("text"): watchlist_entry.get()})
nextrow += 1
(portfolio_entry, portfolio_btn) = create_file_picker("Portfolio", portfolioBtn_Click, labelcol, nextrow)
files.update({portfolio_btn.cget("text"): portfolio_entry.get()})
nextrow += 1
(allocation_entry, allocation_btn) = create_file_picker("Allocation", allocationBtn_Click, labelcol, nextrow)
files.update({allocation_btn.cget("text"): allocation_entry.get()})



root.mainloop()
