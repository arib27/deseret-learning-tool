import tkinter as tk


# create user interface
class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.open_window()
        self.main_frame()

    # create main window
    def open_window(self):
        self.root.title("𐐢𐐯𐑉𐑌 𐐜 𐐔𐐯𐑅𐐨𐑉𐐯𐐻!")
        self.root.geometry("800x600")

    # create frame for main window which shows on opening
    def main_frame(self):
        self.main_frame = tk.Frame(self.root)

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
