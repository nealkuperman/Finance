from tkinter import *
from tkinter import ttk
from label_ttk import *
# from PageTest import runbtn_clicked

__all__ = ["graph_stock_history"]


def graph_stock_history(dictionary):
    for key, value in dictionary.items():
        print("%s: <%s>" % (key, value))
