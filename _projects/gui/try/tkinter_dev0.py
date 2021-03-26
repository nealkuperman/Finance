# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:46:07 2021

@author: Barry
"""
"""
https://stackoverflow.com/questions/40451300/tkinter-in-spyder
"""
import datetime as dt
# from tkcalendar import Calendar, DateEntry
from tkinter import Tk

root = Tk()
root.title("Sum Calculator")
root.geometry('600x300')

# date_entry= DateEntry(root)
# date_entry.pack()
# now= date_entry.get()

def quitbtn_clicked():
    root.destroy()
quitbtn = Button(root, text="Quit",\
                       command=quitbtn_clicked)
quitbtn.grid(row=10,column=4)

StartYearLbl = Label(root, text="Starting Year")
StartYearLbl.grid(row=0,column=0)
StartYear = Entry(root,width=4)
StartYear.insert(0, "1944")
StartYear.grid(row=0,column=1)

endYearLbl = Label(root, text="Ending Year")
endYearLbl.grid(row=1,column=0)
endYear = Entry(root,width=4)
endYear.insert(0, str(dt.datetime.now().date())[0:4])
endYear.grid(row=1,column=1)

stockSourceLbl = Label(root, text="Stock Source")
stockSourceLbl.grid(row=2,column=0)
stockSource = Entry(root,width=10)
stockSource.insert(0, "Yahoo")
stockSource.grid(row=2,column=1)

stockNameLbl = Label(root, text="Stock Name")
stockNameLbl.grid(row=3,column=0)
stockName = Entry(root,width=10)
stockName.insert(0, "NFLX")
stockName.grid(row=3,column=1)

year_range_lbl=Label(root, text="Year Range:")
year_range_lbl.grid(row=4,column=0)

def rangebtn_clicked():
    year_range = int(stockSource.get())- int(StartYear.get())
    year_range_text="Range = " + str(year_range)
    year_range_lbl.configure(text= year_range_text)

rangebtn = Button(root, text="Calc Range", \
                  command=rangebtn_clicked)
rangebtn.grid(row=5,column=0)

root.mainloop()