import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import ttk

import webbrowser

from pathlib import Path

## TO DO
# configure start menu buttons


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
        self.header_font_2 = tkFont.Font(family="Georgia Bold", size=20)
        self.button_font_1 = tkFont.Font(family="Georgia", size=15)
        self.main_text_font = tkFont.Font(family="Georgia", size=12)
        self.text_entry_font = tkFont.Font(family="Noto Sans Deseret", size=23)

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
            font=self.header_font_1,
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
            command=self.main_instructions,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.instructions_button.pack(side="bottom", pady=5)

        # create program start button
        self.start_button = tk.Button(
            self.main_frame,
            text="Begin! - 𐐒𐐀𐐘𐐆𐐤!",
            command=self.begin_menu_frame,
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
    def main_instructions(self):
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
            text="Back - 𐐒𐐈𐐗",
            command=self.go_back,
            bg="#FFFFDB",
            font=self.button_font_1,
        )
        self.back_button.pack(side="bottom", pady=10)

        self.keyboard_instructions_button = tk.Button(
            frame,
            text="Keyboard installation and use - 𐐗𐐀𐐒𐐄𐐡𐐔",
            command=self.open_keyboard_instructions,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom")
        self.show_frame(frame)

    # define keyboard instructions page button function
    def keyboard_instructions(self):
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
            text="Back - 𐐒𐐈𐐗",
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

    # create begin program menu
    def begin_menu_frame(self):
        frame = tk.Frame(self.root, bg="#EDE4BE")

        # create text and buttons
        tk.Label(
            frame,
            text="Choose a learning mode to proceed - 𐐕𐐅𐐞 𐐊 𐐢𐐇𐐡𐐤𐐆𐐥 𐐣𐐄𐐔 𐐓𐐅 𐐑𐐡𐐄𐐝𐐀𐐔",
            font=self.header_font_2,
            bg="#EDE4BE",
        ).pack(side="top", pady=30)

        self.back_button = tk.Button(
            frame,
            text="Back - 𐐒𐐈𐐗",
            command=self.go_back,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom", pady=15)

        img_path = self.DATA_FOLDER / "des_img_2.jpg"
        self.manu_img = Image.open(img_path)
        self.manu_img = ImageTk.PhotoImage(self.manu_img)
        manuscript_img = tk.Label(frame, image=self.manu_img)
        manuscript_img.pack(side="bottom", pady=9)

        tk.Button(
            frame,
            text="Flashcards - 𐐙𐐢𐐈𐐟𐐗𐐉𐐡𐐔𐐞",
            command=self.flashcards_frame,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(pady=9)

        tk.Button(
            frame,
            text="Deseret to Latin Typing - 𐐔𐐇𐐝𐐞𐐡𐐇𐐓 𐐓𐐅 𐐢𐐈𐐓𐐆𐐤 𐐓𐐌𐐑𐐆𐐥",
            command=self.d_to_l_typing_frame,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(pady=9)

        tk.Button(
            frame,
            text="Latin to Deseret Typing - 𐐢𐐈𐐓𐐆𐐤 𐐓𐐅 𐐔𐐇𐐝𐐞𐐡𐐇𐐓 𐐓𐐌𐐑𐐆𐐥",
            command=self.l_to_d_typing_frame,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(pady=9)

        self.show_frame(frame)

    # create flashcard function frame
    def flashcards_frame(self):
        frame = tk.Frame(self.root, bg="#EDE4BE")

        self.back_button = tk.Button(
            frame,
            text="Back - 𐐒𐐈𐐗",
            command=self.go_back,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom", pady=15)

        self.show_frame(frame)

    # create deseret to latin typing function frame
    def d_to_l_typing_frame(self):
        frame = tk.Frame(self.root, bg="#EDE4BE")

        tk.Label(
            frame,
            text="Deseret to Latin Typing practice - 𐐔𐐇𐐝𐐞𐐡𐐇𐐓 𐐓𐐅 𐐢𐐈𐐓𐐆𐐤 𐐓𐐌𐐑𐐆𐐥 𐐑𐐡𐐈𐐗𐐓𐐆𐐝",
            font=self.header_font_2,
            bg="#EDE4BE",
        ).pack(side="top", pady=30)

        tk.Label(
            frame,
            text="Enter the corresponding Latin text for the Deseret shown.",
            font=self.header_font_2,
            bg="#EDE4BE",
        ).pack(side="top", pady=30)

        tk.Label(
            frame,
            text="Here is the example",
            font=self.header_font_1,
            bg="#EDE4BE",
        ).pack(side="top", pady=30)

        self.back_button = tk.Button(
            frame,
            text="Back - 𐐒𐐈𐐗",
            command=self.go_back,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom", pady=15)

        tk.Text(frame, width=20, font=self.text_entry_font).pack(side="bottom", pady=80)

        self.show_frame(frame)

    # create latin to deseret typing function frame
    def l_to_d_typing_frame(self):
        frame = tk.Frame(self.root, bg="#EDE4BE")

        tk.Label(
            frame,
            text="Latin to Deseret Typing practice - 𐐢𐐈𐐓𐐆𐐤 𐐓𐐅 𐐔𐐇𐐝𐐞𐐡𐐇𐐓 𐐓𐐌𐐑𐐆𐐥 𐐑𐐡𐐈𐐗𐐓𐐆𐐝",
            font=self.header_font_2,
            bg="#EDE4BE",
        ).pack(side="top", pady=30)

        tk.Label(
            frame,
            text="Enter the corresponding Deseret text for the Latin shown.",
            font=self.header_font_2,
            bg="#EDE4BE",
        ).pack(side="top", pady=30)

        tk.Label(
            frame,
            text="Here is the example",
            font=self.header_font_1,
            bg="#EDE4BE",
        ).pack(side="top", pady=30)

        self.back_button = tk.Button(
            frame,
            text="Back - 𐐒𐐈𐐗",
            command=self.go_back,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom", pady=15)

        tk.Text(frame, width=20, font=self.text_entry_font).pack(side="bottom", pady=80)

        self.show_frame(frame)
