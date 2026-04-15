import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import webbrowser
from pathlib import Path

## TO DO
# configure start button
# maybe: change paths for .txt, .jpg files into data folder, universalize go_back_frame functions


# create user interface
class Gui:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent  # src/
        self.PROJECT_ROOT = self.BASE_DIR.parent  # project/
        self.DATA_DIR = self.PROJECT_ROOT / "data"  # project/data/
        self.root = tk.Tk()
        self.open_window()
        self.main_frame()

    # create main window
    def open_window(self):
        self.root.title("𐐢𐐯𐑉𐑌 𐐜 𐐔𐐯𐑅𐐨𐑉𐐯𐐻!")
        self.root.geometry("900x600")

    # create frame for main window which shows on opening
    def main_frame(self):
        self.main_frame = tk.Frame(self.root, bg="#EDE4BE")
        self.main_frame.pack(fill="both", expand=True)

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
            command=self.begin_program,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.start_button.pack(side="bottom", pady=5)

        # add image
        img_path = self.DATA_DIR / "des_img.jpg"
        self.fb_img = Image.open(img_path)
        self.fb_img = Image.open("des_img.jpg")
        self.fb_img = ImageTk.PhotoImage(self.fb_img)
        first_book_img = tk.Label(self.main_frame, image=self.fb_img)
        first_book_img.pack(side="bottom", pady=5)

    # define webpage button function
    def open_page(self):
        webbrowser.open("http://faculty.las.illinois.edu/rshosted/deseret.html")

    # define instructions page button function
    def open_instructions(self):
        # hide old frame
        self.main_frame.pack_forget()
        # create new frame that opens on button press
        self.instructions_frame = tk.Frame(self.root, bg="#EDE4BE")
        self.instructions_frame.pack(fill="both", expand=True)

        # fill instructions frame with info
        instr_path = self.DATA_DIR / "program_instructions.txt"
        with open(instr_path, "r", encoding="utf-8") as file:
            instr_text = file.read()

        tk.Label(
            self.instructions_frame,
            text=instr_text,
            font=self.main_text_font,
            bg="#EDE4BE",
        ).pack(side="top", pady=10)

        # create buttons
        self.back_button = tk.Button(
            self.instructions_frame,
            text="Back",
            command=self.frame_back_to_main,
            bg="#FFFFDB",
            font=self.button_font_1,
        )
        self.back_button.pack(side="bottom", pady=10)

        self.keyboard_instructions_button = tk.Button(
            self.instructions_frame,
            text="Keyboard installation and use",
            command=self.open_keyboard_instructions,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.keyboard_instructions_button.pack(side="bottom", pady=10)

    # create function that returns page to main frame
    def frame_back_to_main(self):
        # hide old frame
        self.instructions_frame.pack_forget()
        # open new frame
        self.main_frame.pack(fill="both", expand=True)

    # define keyboard instructions page button function
    def open_keyboard_instructions(self):
        # hide old frame
        self.instructions_frame.pack_forget()
        # create keyboard instructions frame
        self.keyboard_instr_frame = tk.Frame(self.root, bg="#EDE4BE")
        self.keyboard_instr_frame.pack(fill="both", expand=True)

        # fill keyboard frame with info
        key_instr_path = self.DATA_DIR / "keyboard_installation.txt"
        with open(key_instr_path, "r", encoding="utf-8") as file:
            key_instr_text = file.read()

        tk.Label(
            self.keyboard_instr_frame,
            text=key_instr_text,
            font=self.main_text_font,
            bg="#EDE4BE",
        ).pack(side="top")

        # add back button
        self.back_button = tk.Button(
            self.keyboard_instr_frame,
            text="Back",
            command=self.frame_back_to_instr,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.back_button.pack(side="top")

    # create function that returns page to instructions frame
    def frame_back_to_instr(self):
        # hide old frame
        self.keyboard_instr_frame.pack_forget()
        # open new frame
        self.instructions_frame.pack(fill="both", expand=True)

    # define program start button function
    def begin_program(self):
        pass
