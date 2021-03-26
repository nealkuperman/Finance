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

    def __init__(self, parent, btn_lbl, btn_col, btn_lbl_col, row):
        self.parent = parent
        self.create_file_picker(btn_lbl, btn_col, btn_lbl_col, row)

    def create_ttklabel(self, lbl_txt, row, col):
        self.lbl = ttk.Label(self.parent, text=lbl_txt)
        self.lbl.grid(row=row, column=col)

    def create_ttkbutton(self, btn_lbl, btn_col, row):
        self.btn = ttk.Button(self.parent,
                                     text=btn_lbl,
                                     command=self.Btn_Click)
        self.btn.grid(column=btn_col, row=row)

    def create_file_picker(self, btn_lbl, btn_col, btn_lbl_col, row):
        self.create_ttkbutton(btn_lbl, btn_col, row)
        self.create_ttklabel("No File Selected", row, btn_lbl_col)

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Python files",
                                                          "*.py*"),
                                                         ("all files",
                                                          "*.*")))
        if self.filename != '':
            self.lbl.configure(text=self.filename)

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
    watchlist_file_picker = FilePicker(root, "Watchlist", button_collum, button_lbl_co, nextrow)
    # showinfo(title="Selected File", message=filename)

    root.mainloop()
