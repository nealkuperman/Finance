from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from label_ttk import *
# from PageTest import runbtn_clicked

__all__ = ["graph_stock_history"]


def graph_stock_history(dictionary):
    items = []
    for key, value in dictionary.items():
        formatted = "%s: <%s>" % (key, value)
        print(formatted)
        items.append(formatted)

    messagebox.showinfo(title="Data", message='\n'.join(items))
