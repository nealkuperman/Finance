from StockHistoryStub0 import *
from StockPortfolioStub0 import *
import tkinter as tk
from label_ttk import *

__all__ = ["Menu"]

'''
TO DO
1. Ignore Page 2
2. For StockHistoryPage: 
    a. Input fields for Start Date, End Date, Display Field, Data Source, Stock Names, Ticker Symbols,
        i. Start Date: Date Entry
        ii. End Date: Date Entry
        iii. Display Field: Drop Down Box 
        iv. Data Source: Drop Down Box
        v. Stock Names: Entry
        vi. Ticker Symbols: Entry
    b. Run Button call Neal's function to plot
        i. Create new file mimicking Neal's file and send these values to a the file
    c. Quit Button which ends the program
'''


class tkinterApp(tk.Tk):
    LARGEFONT = ("Verdana", 35)

    start_date = ""

    page_button_col = 0
    label_col = page_button_col + 1
    entry_col = label_col + 1
    data_source_names = ["Data One", "Data Two", "Data Three"]
    display_field_names = ["Field One", "Field Two", "Field Three"]

    previous_frame = None
    current_frame = None
    frames = {}

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.current_frame = Menu
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Menu, StockHistory, StockPortfolio):
            frame = F(container, self)

            # initializing frame of that object from
            # Menu, StockHistoryPage, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Menu)
        # to display the current frame passed as
    # parameter

    def show_frame(self, frame_to_show):
        self.previous_frame = self.current_frame
        frame = self.frames[frame_to_show]
        frame.tkraise()
        self.current_frame = frame_to_show
        self.title(frame_to_show.PAGE_NAME)
        # self.title(self.camel_case_split(frame_to_show.__name__))
    '''
    def camel_case_split(self, string):
        words = [[string[0]]]

        for c in string[1:]:
            if words[-1][-1].islower() and c.isupper():
                words.append(list(c))
            else:
                words[-1].append(c)

        return [''.join(word) for word in words]
   '''
# first window frame Menu


class Menu(tk.Frame):
    PAGE_NAME = "Menu"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = create_label(self, text="Menu", row=0, column=4)
        label.configure(font=controller.LARGEFONT)
        label.grid(padx=10, pady=10)

        stock_history_button = create_button(self, "Stock History", lambda: controller.show_frame(StockHistory),
                                                row=1, column=1)
        stock_history_button.grid(padx=10, pady=10)

        # button to show frame 2 with text layout2
        stock_portfolio_button = create_button(self, "Stock Portfolio",
                                                  lambda: controller.show_frame(StockPortfolio), row=2, column=1)
        stock_portfolio_button.grid(padx=10, pady=10)

        self.quitbtn = create_button(self, "Quit", self.quitbtn_clicked, 11, 4)

    def quitbtn_clicked(self):
        app.destroy()


if __name__ == "__main__":
    pass

# Driver Code
app = tkinterApp()
app.mainloop()
