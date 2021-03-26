from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo

__all__ = ["create_ttklabel"]


class FilePicker():
    parent = None
    btn = None
    lbl = None
    filename = ""

    def __init__(self, parent, btn_lbl, entry_width, btn_col, btn_lbl_col, row):
        self.parent = parent
        self.create_file_picker(btn_lbl, entry_width, btn_col, btn_lbl_col, row)

    def create_ttkentry(self, lbl_txt, entry_width, row, col):
        self.lbl = ttk.Entry(self.parent, width=entry_width)
        self.lbl.grid(row=row, column=col)
        self.lbl.insert(0, lbl_txt)
        self.lbl.config(state=DISABLED)

    def create_ttkbutton(self, btn_lbl, btn_col, row):
        self.btn = ttk.Button(self.parent,
                                     text=btn_lbl,
                                     command=self.Btn_Click)
        self.btn.grid(column=btn_col, row=row)

    def create_file_picker(self, btn_lbl, entry_width, btn_col, btn_lbl_col, row):
        self.create_ttkbutton(btn_lbl, btn_col, row)
        self.create_ttkentry("No File Selected", entry_width, row, btn_lbl_col)

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Python files",
                                                          "*.py*"),
                                                         ("all files",
                                                          "*.*")))
        if self.filename != '':
            self.lbl.config(state=NORMAL)
            self.lbl.delete(0, END)
            self.lbl.insert(0, self.filename)
            self.lbl.config(state=DISABLED)

    def Btn_Click(self):
        self.browseFiles()


if __name__ == "__main__":
    root = Tk()
    root.title("Sum Calculator")
    root.geometry('600x300')
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    nextrow = 0
    button_collum = 0
    button_lbl_co = button_collum + 1
    PATH_ENTRY_WIDTH = 40

    nextrow += 1
    watchlist_file_picker = FilePicker(root, "Watchlist", PATH_ENTRY_WIDTH, button_collum, button_lbl_co, nextrow)
    # showinfo(title="Selected File", message=filename)

    root.mainloop()
