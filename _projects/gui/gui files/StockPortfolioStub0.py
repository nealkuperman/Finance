import tkinter as tk
from label_ttk import *
__all__ = ["StockPortfolio"]


class StockPortfolio(tk.Frame):
    FRAME_NAME = "Stock Portfolio"
    next_row = 0
    controller = None
    parent_frame = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.next_row += 1
        back_button = create_button(self, "Back", lambda: controller.show_frame(controller.previous_frame),
                                    self.next_row, controller.page_button_col)
        self.next_row = 0
