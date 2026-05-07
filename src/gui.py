import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont

import webbrowser

from pathlib import Path

from cards import load_cards

## TO DO
# configure start button


# create user interface
class Gui:
    def __init__(self):
        self.SRC_FOLDER = Path(__file__).resolve().parent  # src/
        self.PROJ_FOLDER = self.SRC_FOLDER.parent  # project/
        self.DATA_FOLDER = self.PROJ_FOLDER / "data"  # project/data/

        self.root = tk.Tk()
        self.frame_stack = []
        self.current_frame = None

        self.open_window()
        self.main_window_frame()

    # create main window
    def open_window(self):
        self.root.title("𐐢𐐯𐑉𐑌 𐐜 𐐔𐐯𐑅𐐨𐑉𐐯𐐻!")
        self.root.geometry("900x600")

    # create frame for main window which shows on opening
    def main_window_frame(self):
        self.main_frame = tk.Frame(self.root, bg="#EDE4BE")
        self.show_frame(self.main_frame)

        # create custom fonts for gui
        self.header_font_1 = tkFont.Font(family="Georgia Bold", size=32)
        self.header_font_2 = tkFont.Font(family="Georgia Bold", size=32)
        self.button_font_1 = tkFont.Font(family="Georgia", size=15)
        self.main_text_font = tkFont.Font(family="Georgia", size=12)

        # create text
        tk.Label(
            self.main_frame,
            text="Deseret Learning Tool",
            font=self.header_font_1,
            bg="#EDE4BE",
        ).pack(side="top", pady=5)
        tk.Label(
            self.main_frame,
            text="𐐔𐐯𐑅𐑆𐑉𐐯𐐻 𐐢𐐯𐑉𐑌𐐮𐑍 𐐓𐐭𐑊",
            font=self.header_font_2,
            bg="#EDE4BE",
        ).pack(side="top", pady=5)

        # create program exit button
        self.quit_button = tk.Button(
            self.main_frame,
            text="Quit - 𐐗𐐎𐐆𐐓",
            command=self.root.destroy,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.quit_button.pack(side="bottom", pady=5)

        # create webpage link button
        self.information_button = tk.Button(
            self.main_frame,
            text="Illinois Deseret Consortium (more information!) - 𐐆𐐔𐐗",
            command=self.open_page,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.information_button.pack(side="bottom", pady=5)

        # create instructions page button
        self.instructions_button = tk.Button(
            self.main_frame,
            text="Program Instructions - 𐐑𐐡𐐄𐐘𐐡𐐈𐐣 𐐆𐐤𐐝𐐓𐐡𐐊𐐗𐐟𐐆𐐤𐐞",
            command=self.open_instructions,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.instructions_button.pack(side="bottom", pady=5)

        # create program start button
        self.start_button = tk.Button(
            self.main_frame,
            text="Begin! - 𐐒𐐀𐐘𐐆𐐤!",
            command=load_cards,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.start_button.pack(side="bottom", pady=5)

        # add image
        img_path = self.DATA_FOLDER / "des_img.jpg"
        self.fb_img = Image.open(img_path)
        self.fb_img = ImageTk.PhotoImage(self.fb_img)
        first_book_img = tk.Label(self.main_frame, image=self.fb_img)
        first_book_img.pack(side="bottom", pady=5)

    # define webpage button function
    def open_page(self):
        webbrowser.open("http://faculty.las.illinois.edu/rshosted/deseret.html")

    # define instructions page button function
    def open_instructions(self):
        frame = tk.Frame(self.root, bg="#EDE4BE")

        # fill instructions frame with info
        instr_path = self.DATA_FOLDER / "program_instructions.txt"
        with open(instr_path, "r", encoding="utf-8") as file:
            instr_text = file.read()

        tk.Label(
            frame,
            text=instr_text,
            font=self.main_text_font,
            bg="#EDE4BE",
        ).pack(side="top", pady=10)

        # create buttons
        self.back_button = tk.Button(
            frame,
            text="Back",
            command=self.go_back,
            bg="#FFFFDB",
            font=self.button_font_1,
        )
        self.back_button.pack(side="bottom", pady=10)

        self.keyboard_instructions_button = tk.Button(
            frame,
            text="Keyboard installation and use",
            command=self.open_keyboard_instructions,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom")
        self.show_frame(frame)

    # define keyboard instructions page button function
    def open_keyboard_instructions(self):
        frame = tk.Frame(self.root, bg="#EDE4BE")

        # fill keyboard frame with info
        key_instr_path = self.DATA_FOLDER / "keyboard_installation.txt"
        with open(key_instr_path, "r", encoding="utf-8") as file:
            key_instr_text = file.read()

        tk.Label(
            frame,
            text=key_instr_text,
            font=self.main_text_font,
            bg="#EDE4BE",
        ).pack(side="top")

        # add back button
        self.back_button = tk.Button(
            frame,
            text="Back",
            command=self.go_back,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom", pady=10)
        self.show_frame(frame)

    # create function that shows new frame
    def show_frame(self, new_frame):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
            self.frame_stack.append(self.current_frame)
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    # create function that goes back a frame
    def go_back(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        if self.frame_stack:
            self.current_frame = self.frame_stack.pop()
            self.current_frame.pack(fill="both", expand=True)

    # define program start button function
    def begin_program(self):
        pass
