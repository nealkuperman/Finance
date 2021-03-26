from tkinter import *
from tkinter import ttk
from tkinter import filedialog

__all__ = ["create_ttklabel"]

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


def create_file_picker(parent, btn_lbl, command, labelcol, nextrow):
    file_picker_btn = ttk.Button(parent,
                            text=btn_lbl,
                            command=command)
    file_picker_lbl = create_ttklabel(parent, "No File Selected", nextrow, entrycol)
    file_picker_btn.grid(column=labelcol, row=nextrow)
    return file_picker_lbl, file_picker_btn


def browseFiles(file_control):
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Python files",
                                                      "*.py*"),
                                                     ("all files",
                                                      "*.*")))
    if filename != '':
        file_control.configure(text=filename)


# def watchlist_entry_change():
    # watchlist_lbl.configure(text=watch)


def watchListBtn_Click():
    browseFiles(watchlist_lbl)


if __name__ == "__main__":
    root = Tk()
    root.title("Sum Calculator")
    root.geometry('600x300')
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    nextrow = 0
    labelcol = 0
    entrycol = labelcol + 1
    PATH_ENTRY_WIDTH = 40

    nextrow += 1
    (watchlist_lbl, watchlist_btn) = create_file_picker(root, "Watchlist", watchListBtn_Click, labelcol, nextrow)
    # watchlist_entry.bind("<FocusOut>", watchlist_entry_change)

    root.mainloop()
