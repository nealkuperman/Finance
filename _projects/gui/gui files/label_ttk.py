import datetime as dt
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry

__all__ = ["create_entry", "create_button", "create_label", "create_dateentry", "create_combobox",
           "create_optionmenu", "LabeledFilePicker", "LabeledEntry", "LabeledLabel", "LabeledDateEntry",
           "LabeledComboBox", "LabeledOptionMenu", "TWO_DIGIT_YEAR_FORMAT", "FOUR_DIGIT_YEAR_FORMAT"]

TWO_DIGIT_YEAR_FORMAT = 'MM/dd/yy'
FOUR_DIGIT_YEAR_FORMAT = 'MM/dd/yyyy'


def create_entry(parent, entry_text, entry_width, row=0, column=0, enabled=True):
    entry = ttk.Entry(parent, width=entry_width)
    entry.grid(row=row, column=column)
    entry.insert(0, entry_text)
    if not enabled:
        entry.config(state=DISABLED)
    return entry


def create_button(parent, text, command, row=0, column=0):
    button = ttk.Button(parent,
                        text=text,
                        command=command)
    button.grid(column=column, row=row)
    return button


def create_label(parent, text, row=0, column=0):
    label = ttk.Label(parent, text=text)
    label.grid(row=row, column=column)
    return label


def create_dateentry(parent, mindate, maxdate, start_date, row=0, column=0, date_pattern=FOUR_DIGIT_YEAR_FORMAT):
    # STARTING DATE DOES NOT HAVE TO BE MINDATE
    date_entry = DateEntry(parent, width=11, background='darkblue', foreground='white', borderwidth=2, mindate=mindate,
                           maxdate=maxdate, date_pattern=date_pattern, day=start_date.day, month=start_date.month,
                           year=start_date.year)
    date_entry.grid(row=row, column=column)
    return date_entry


def create_combobox(parent, values, row=0, column=0):
    combo_box = ttk.Combobox(parent, values=values)
    combo_box.grid(row=row, column=column)
    return combo_box


def create_optionmenu(parent, value, options, row=0, column=0):
    option_menu = ttk.OptionMenu(parent, value, options[0], *options)
    option_menu.grid(row=row, column=column)
    return option_menu


def create_checkbutton(parent, text, variable, command=None, onvalue=1, offvalue=0, row=0, column=0):
    button = ttk.Checkbutton(parent, text=text, variable=variable, command=command, onvalue=onvalue, offvalue=offvalue)
    button.grid(row=row, column=column)
    button.config()
    return button


class LabeledFilePicker:
    parent = None
    button = None
    entry = None
    NO_FILE_TEXT = "No File Selected"
    filename = ""

    def __init__(self, parent, btn_lbl, entry_width, btn_col, btn_lbl_col, row):
        self.parent = parent
        self.create_file_picker(btn_lbl, entry_width, btn_col, btn_lbl_col, row)

    def create_file_picker(self, btn_lbl, entry_width, btn_col, btn_lbl_col, row):
        self.button = create_button(self.parent, btn_lbl, self.browse_files, row, btn_col)
        self.entry = create_entry(self.parent, self.NO_FILE_TEXT, entry_width, row, btn_lbl_col, False)

    def browse_files(self):
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


class LabeledEntry:
    parent = None
    label = None
    entry = None
    enabled = None

    def __init__(self, parent, label_text, labelcol, entry_txt, entrycol, entry_width,  row, enabled=True):
        self.parent = parent
        self.enabled = enabled
        self.entry = create_entry(self.parent, entry_txt, entry_width, row, entrycol, self.enabled)
        self.label = create_label(self.parent, label_text, row, labelcol)


class LabeledLabel:
    parent = None
    label = None
    label2 = None

    def __init__(self, parent, label_text, labelcol, label2_text, label2col,  row):
        self.parent = parent
        self.label = create_label(self.parent, label_text, row, labelcol)
        self.label2 = create_label(self.parent, label2_text, row, label2col)


class LabeledDateEntry:
    parent = None
    date_entry = None
    label = None

    def __init__(self, parent, mindate, maxdate, start_date, label_text, row, label_column, entry_column,
                 date_pattern=FOUR_DIGIT_YEAR_FORMAT):
        self.parent = parent
        self.label = create_label(self.parent, label_text, row, label_column)
        self.date_entry = create_dateentry(self.parent, mindate, maxdate, start_date, row, entry_column, date_pattern)


class LabeledComboBox:
    parent = None
    combo_box = None
    label = None

    def __init__(self, parent, label_text, row, label_column, values, combo_box_column):
        self.parent = parent
        self.label = create_label(self.parent, label_text, row, label_column)
        self.combo_box = create_combobox(self.parent, values, row=row, column=combo_box_column)


class LabeledOptionMenu:
    parent = None
    option_menu = None
    label = None

    def __init__(self, parent, label_text, row, value, label_column, options, option_menu_column):
        self.parent = parent
        self.label = create_label(self.parent, label_text, row, label_column)
        self.option_menu = create_optionmenu(self.parent, value, options, row=row, column=option_menu_column)


if __name__ == "__main__":
    root = Tk()
    root.title("Sum Calculator")
    root.geometry('600x300')
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    next_row = 0
    lbl_col = 0
    entry_col = lbl_col + 1
    PATH_ENTRY_WIDTH = 40

    labeled_entry = LabeledEntry(root, "LABEL TEXT", lbl_col, "ENTRY TEXT", entry_col, 10, next_row, True)
    next_row += 1
    watchlist_file_picker = LabeledFilePicker(root, "Watchlist", PATH_ENTRY_WIDTH, next_row, lbl_col, entry_col)
    next_row += 1
    labeled_label = LabeledLabel(root, "Label 1", lbl_col, "Label 2", entry_col, next_row)
    next_row += 1
    calendar_entry = LabeledDateEntry(root, dt.date(year=1944, month=6, day=11), dt.date.today(),
                                  dt.date(year=1944, month=6, day=11), "Date", next_row, lbl_col, entry_col)
    next_row += 1
    vals = ["One", "Two", "Three"]
    combobox = LabeledComboBox(root, "Combo Box", next_row, lbl_col, vals, entry_col)
    next_row += 1
    option_menu = LabeledOptionMenu(root, "Option Menu", next_row, StringVar(), lbl_col, vals, entry_col)
    next_row += 1
    clicked = BooleanVar()
    def check_box_clicked():
        print("passed")
    check_box = create_checkbutton(root, "Click Me", clicked, command=None, onvalue=True, offvalue=False, row=next_row, column=0)


    #afgsd = LabeledEntry()
    # showinfo(title="Selected File", message=filename)

    root.mainloop()
