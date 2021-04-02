import datetime as dt
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkcalendar import Calendar, DateEntry

__all__ = ["create_ttklabel"]


def create_ttkentry(parent, entry_text, entry_width, row, column, enabled):
    entry = ttk.Entry(parent, width=entry_width)
    entry.grid(row=row, column=column)
    entry.insert(0, entry_text)
    if not enabled:
        entry.config(state=DISABLED)
    return entry


def create_ttkbutton(parent, btn_lbl, command, row, btn_col):
    button = ttk.Button(parent,
                        text=btn_lbl,
                        command=command)
    button.grid(column=btn_col, row=row)
    return button


def create_ttklabel(parent, label_text, column, row):
    label = ttk.Label(parent, text=label_text)
    label.grid(row=row, column=column)
    return label


'''class CreateLabel():
    def __init__(self, parent, label_text, column, row):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=column)
        '''


class LabeledFilePicker():
    parent = None
    button = None
    entry = None
    NO_FILE_TEXT = "No File Selected"
    filename = ""

    def __init__(self, parent, btn_lbl, entry_width, btn_col, btn_lbl_col, row):
        self.parent = parent
        self.create_file_picker(btn_lbl, entry_width, btn_col, btn_lbl_col, row)

    def create_file_picker(self, btn_lbl, entry_width, btn_col, btn_lbl_col, row):
        self.button = create_ttkbutton(self.parent, btn_lbl, self.Btn_Click, row, btn_col)
        self.entry = create_ttkentry(self.parent, self.NO_FILE_TEXT, entry_width, row, btn_lbl_col, False)

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Python files",
                                                          "*.py*"),
                                                         ("all files",
                                                          "*.*")))
        if self.filename != '':
            self.entry.config(state=NORMAL)
            self.entry.delete(0, END)
            self.entry.insert(0, self.filename)
            self.entry.config(state=DISABLED)

    def Btn_Click(self):
        self.browseFiles()


class LabeledEntry():
    parent = None
    label = None
    entry = None
    enabled = None

    def __init__(self, parent, label_text, labelcol, entry_txt, entrycol, entry_width,  row, enabled):
        self.parent = parent
        self.enabled = enabled
        self.entry = create_ttkentry(self.parent, entry_txt, entry_width, row, entrycol, self.enabled)
        self.label = create_ttklabel(self.parent, label_text, labelcol, row)


class LabeledLabel():
    parent = None
    label = None
    label2 = None

    def __init__(self, parent, label_text, labelcol, label2_text, label2col,  row):
        self.parent = parent
        self.label = create_ttklabel(self.parent, label_text, labelcol, row)
        self.label2 = create_ttklabel(self.parent, label2_text, label2col, row)


class LabeledDateEntry():
    parent = None
    date_entry = None
    label = None

    def __init__(self, parent, mindate, maxdate, start_date, label_text, row, label_column, entry_column):
        self.parent = parent
        self.label = create_ttklabel(self.parent, label_text, label_column, row)
        self.create_ttkdateentry(mindate, maxdate, start_date, row, entry_column)

    def create_ttkdateentry(self, mindate, maxdate, start_date, row, column):
        # STARTING DATE DOES NOT HAVE TO BE MINDATE
        self.date_entry = DateEntry(self.parent, width=11,
                            background='darkblue',
                            foreground='white',
                            borderwidth=2,
                            mindate=mindate,
                            maxdate=maxdate,
                            date_pattern='MM/dd/yyyy',
                            day=start_date.day,
                            month=start_date.month,
                            year=start_date.year)
        self.date_entry.grid(row=row, column=column)


if __name__ == "__main__":
    root = Tk()
    root.title("Sum Calculator")
    root.geometry('600x300')
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    nextrow = 0
    lbl_col = 0
    entry_col = lbl_col + 1
    PATH_ENTRY_WIDTH = 40

    labeled_entry = LabeledEntry(root, "LABEL TEXT", lbl_col, "ENTRY TEXT", entry_col, 10, nextrow, True)
    nextrow += 1
    watchlist_file_picker = LabeledFilePicker(root, "Watchlist", PATH_ENTRY_WIDTH, nextrow, lbl_col, entry_col)
    nextrow += 1
    labeled_label = LabeledLabel(root, "Label 1", lbl_col, "Label 2", entry_col, nextrow)
    nextrow += 1
    date_entry = LabeledDateEntry(root, dt.date(year=1944, month=6, day=11), dt.date.today(), dt.date(year=1944, month=6, day=11), "Date", nextrow, lbl_col, entry_col)
    #afgsd = LabeledEntry()
    # showinfo(title="Selected File", message=filename)

    root.mainloop()
