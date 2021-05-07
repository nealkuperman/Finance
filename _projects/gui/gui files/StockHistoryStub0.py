import datetime as dt
import tkinter as tk
from tkinter import ttk
from label_ttk import *
from mimic_file import *
__all__ = ["StockHistory"]


# second window frame StockHistoryPage
class StockHistory(tk.Frame):
    FRAME_NAME = "Stock History"
    next_row = 0
    end_date = None
    start_date = None
    START_DATE_LABEL = "Start Date"
    END_DATE_LABEL = "End Date"
    DISPLAY_FIELD_LABEL = "Display Field"
    DATA_SOURCE_LABEL = "Data Source"
    STOCK_NAME_LABEL = "Stock Name"
    TICKER_SYMBOL_LABEL = "Ticker Symbol"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        back_button = create_button(self, "Back", lambda: controller.show_frame(controller.previous_frame),
                                    self.next_row, controller.page_button_col)

        self.next_row = 0

        today = dt.date.today()

        start_date_mindate = dt.date(year=1944, month=6, day=11)
        start_date_maxdate = today
        self.start_date = LabeledDateEntry(self, start_date_mindate, start_date_maxdate, start_date_mindate,
                                           self.START_DATE_LABEL, self.next_row, controller.label_col,
                                           controller.entry_col, date_pattern=FOUR_DIGIT_YEAR_FORMAT)

        self.next_row += 1
        end_date_mindate = dt.date(year=1944, month=6, day=11)
        end_date_maxdate = today
        self.end_date = LabeledDateEntry(self, end_date_mindate, end_date_maxdate, today, self.END_DATE_LABEL,
                                         self.next_row, controller.label_col, controller.entry_col,
                                         date_pattern=FOUR_DIGIT_YEAR_FORMAT)

        self.next_row += 1
        self.display_field = LabeledOptionMenu(self, self.DISPLAY_FIELD_LABEL, self.next_row, tk.StringVar(),
                                               controller.label_col, controller.display_field_names,
                                               controller.entry_col)
        self.next_row += 1
        self.data_source = LabeledOptionMenu(self, self.DATA_SOURCE_LABEL, self.next_row, tk.StringVar(), controller.label_col,
                                             controller.data_source_names, controller.entry_col)
        self.next_row += 1
        self.stock_name = LabeledEntry(self, self.STOCK_NAME_LABEL, controller.label_col, "", controller.entry_col, 10,
                                       self.next_row, True)
        self.next_row += 1
        self.ticker_symbol = LabeledEntry(self, self.TICKER_SYMBOL_LABEL, controller.label_col, "",
                                          controller.entry_col, 10, self.next_row, True)

        self.next_row = 0
        self.runbtn = create_button(self, "Run", lambda: runbtn_clicked(self), row=10, column=4)


def runbtn_clicked(stock_page):
    values = {}
    values[stock_page.START_DATE_LABEL] = stock_page.start_date.date_entry.get()
    values[stock_page.END_DATE_LABEL] = stock_page.end_date.date_entry.get()
    values[stock_page.DISPLAY_FIELD_LABEL] = stock_page.display_field.option_menu.cget('text')
    values[stock_page.DATA_SOURCE_LABEL] = stock_page.data_source.option_menu.cget('text')
    values[stock_page.STOCK_NAME_LABEL] = stock_page.stock_name.entry.get()
    values[stock_page.TICKER_SYMBOL_LABEL] = stock_page.ticker_symbol.entry.get()

    graph_stock_history(values)
