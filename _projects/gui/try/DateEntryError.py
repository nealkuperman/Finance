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
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

root = Tk()
root.title("Sum Calculator")
root.geometry('200x200')

StartDatelbl = ttk.Label(root,  width=15, text='Start date')
StartDatelbl.grid (row=1, column=0)

mindate = dt.date(year=1944, month=6, day=11)
maxdate = dt.date.today()

def dateentry_view():
  def print_sel():
      print(StartDate.get_date())

  x=ttk.Label(root, text='Choose date')#.pack(padx=10, pady=10)
  x.grid (row=2, column=0)
  y=ttk.Button(root, text="ok", command=print_sel).pack()
  y.grid (row=2, column=1)

  StartDate = DateEntry(root, width=11, \
                              background='darkblue', \
                              foreground='white', \
                              borderwidth=2, \
                              date_pattern='mm/dd/yyyy',\
                              mindate=mindate, maxdate=maxdate,\
                              year=1944)
  StartDate.grid (row=2, column=3)

ttk.Button(root, text='DateEntry', command=dateentry_view) #.pack(padx=10, pady=10)

root.mainloop()