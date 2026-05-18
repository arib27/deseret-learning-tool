import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import ttk

import webbrowser

from pathlib import Path

from src.typing_mode import TypingPractice
from src.cards import load_cards, save_cards, update_card, get_due_cards


# create user interface
class Gui:
    def __init__(self):
        self.SRC_FOLDER = Path(__file__).resolve().parent  # src/
        self.PROJ_FOLDER = self.SRC_FOLDER.parent  # project/
        self.DATA_FOLDER = self.PROJ_FOLDER / "data"  # project/data/

        self.root = tk.Tk()
        self.frame_stack = []
        self.current_frame = None

        # initialize flashcards
        self.current_day = 0
        self.cards_path = self.DATA_FOLDER / "alphabet.json"
        self.cards = load_cards(self.cards_path)

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
        self.header_font_3 = tkFont.Font(family="Georgia", size=16)
        self.button_font_1 = tkFont.Font(family="Georgia", size=15)
        self.main_text_font = tkFont.Font(family="Georgia", size=12)
        self.deseret_font = tkFont.Font(family="Noto Sans Deseret", size=23)

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
            command=self.start_program_menu_frame,
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

    # create instructions page
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

        tk.Label(
            frame,
            text="𐐛𐐰𐑌𐐿 𐐷𐐭 𐐻𐐭 𐐑𐑉𐐱𐑁. 𐐡𐐴𐐲𐑌 𐐗. 𐐟𐐱𐑅𐐻𐐯𐐼 𐐰𐑌𐐼 𐐔𐑉. 𐐤𐐨𐑊 𐐔𐐩𐑂𐐮𐑅 𐑁𐐬𐑉 𐑃𐐩𐑉 𐐸𐐯𐑊𐐹 𐐱𐑌 𐑄𐐮𐑅 𐐹𐑉𐐱𐐾𐐯𐐿𐐻!",
            font=self.header_font_3,
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
            command=self.keyboard_instructions,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom")
        self.show_frame(frame)

    # create keyboard instructions page
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
    def start_program_menu_frame(self):
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
        manuscript_img.pack(side="bottom", pady=20)

        tk.Button(
            frame,
            text="Flashcards - 𐐙𐐢𐐈𐐟𐐗𐐉𐐡𐐔𐐞",
            command=self.flashcards_frame,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(pady=30)

        tk.Button(
            frame,
            text="Spelling and Typing - 𐐝𐐑𐐇𐐢𐐆𐐥 𐐈𐐤𐐔 𐐓𐐌𐐑𐐆𐐥",
            command=self.typing_frame,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(pady=15)

        self.show_frame(frame)

    # create typing function page
    def typing_frame(self):
        frame = tk.Frame(self.root, bg="#EDE4BE")

        tk.Label(
            frame,
            text="Spelling and typing practice - 𐐝𐐑𐐇𐐢𐐆𐐥 𐐈𐐤𐐔 𐐓𐐌𐐑𐐆𐐥 𐐑𐐡𐐈𐐗𐐓𐐆𐐝",
            font=self.header_font_2,
            bg="#EDE4BE",
        ).pack(side="top", pady=5)

        tk.Label(
            frame,
            text="Enter the corresponding Latin or Deseret text for the example shown.",
            font=self.button_font_1,
            bg="#EDE4BE",
        ).pack(side="top", pady=5)

        # create separate settings buttons areas
        settings_container = tk.Frame(frame, bg="#EDE4BE")
        settings_container.pack(side="top", pady=10, fill="x")

        settings_frame_left = tk.Frame(settings_container, bg="#EDE4BE")
        settings_frame_left.pack(side="left", expand=True)

        settings_frame_right = tk.Frame(settings_container, bg="#EDE4BE")
        settings_frame_right.pack(side="right", expand=True)

        self.mode_var = tk.StringVar(value="deseret_to_latin")

        tk.Radiobutton(
            settings_frame_left,
            text="Deseret → Latin",
            font=self.main_text_font,
            variable=self.mode_var,
            value="deseret_to_latin",
            bg="#EDE4BE",
            highlightthickness=0,
        ).pack(side="top", pady=2, anchor="w")

        tk.Radiobutton(
            settings_frame_left,
            text="Latin → Deseret",
            font=self.main_text_font,
            variable=self.mode_var,
            value="latin_to_deseret",
            bg="#EDE4BE",
            highlightthickness=0,
        ).pack(side="top", pady=2, anchor="w")

        # choose difficulty
        self.difficulty_var = tk.IntVar(value=1)

        tk.Label(
            settings_frame_right,
            text="Difficulty: 1 (easy) -> 3 (hard)",
            font=self.main_text_font,
            bg="#EDE4BE",
        ).pack(side="top", pady=2)

        ttk.Combobox(
            settings_frame_right,
            textvariable=self.difficulty_var,
            values=[1, 2, 3],
            state="readonly",
            width=5,
        ).pack(side="top", pady=2)

        # start practice
        tk.Button(
            frame,
            text="Start Practice",
            font=self.button_font_1,
            bg="#FFFFDB",
            command=self.start_practice,
        ).pack(side="top", pady=15)

        # prompt
        self.question_label = tk.Label(
            frame,
            text="",
            font=self.deseret_font,
            bg="#EDE4BE",
        )
        self.question_label.pack(side="top", pady=10)

        # feedback
        self.result_label = tk.Label(
            frame,
            text="",
            font=self.button_font_1,
            bg="#EDE4BE",
        )
        self.result_label.pack(side="top", pady=10)

        # text entry box
        self.answer_entry = tk.Text(frame, width=20, height=1, font=self.deseret_font)
        self.answer_entry.pack(side="top", pady=10)

        # back button
        self.back_button = tk.Button(
            frame,
            text="Back - 𐐒𐐈𐐗",
            command=self.go_back,
            font=self.button_font_1,
            bg="#FFFFDB",
        )
        self.back_button.pack(side="bottom", pady=10)

        # submit button
        tk.Button(
            frame,
            text="Enter Answer",
            font=self.button_font_1,
            bg="#FFFFDB",
            command=self.submit_answer,
        ).pack(side="bottom", pady=25)

        self.show_frame(frame)

    # create function to start typing practice
    def start_practice(self):
        self.practice = TypingPractice(
            mode=self.mode_var.get(), difficulty=self.difficulty_var.get()
        )
        self.load_question()

    # create function to show next question (typing)
    def load_question(self):
        question = self.practice.next_question()
        self.question_label.config(text=question)
        self.answer_entry.delete("1.0", tk.END)
        self.result_label.config(text="")

    # create function to submit user answer (typing)
    def submit_answer(self):
        user_answer = self.answer_entry.get("1.0", "end-1c")
        correct = self.practice.grade_answer(user_answer)
        correct_answer = self.practice.get_answer()

        if correct:
            if self.practice.mode == "deseret_to_latin":
                self.result_label.config(
                    text="Correct!",
                    font=self.deseret_font,
                )
                self.root.after(1200, self.load_question)

            if self.practice.mode == "latin_to_deseret":
                self.result_label.config(
                    text=f"Correct! Possible answers: {correct_answer}",
                    font=self.deseret_font,
                )
                self.root.after(2500, self.load_question)

        else:
            self.result_label.config(
                text=f"Incorrect! Right answer: {correct_answer}",
                font=self.deseret_font,
            )
            self.root.after(2500, self.load_question)

    # create flashcard function page
    def flashcards_frame(self):
        frame = tk.Frame(self.root, bg="#EDE4BE")

        tk.Label(
            frame,
            text="Flashcard practice - 𐐙𐐢𐐈𐐟𐐗𐐉𐐡𐐔 𐐑𐐡𐐈𐐗𐐓𐐆𐐝",
            font=self.header_font_2,
            bg="#EDE4BE",
        ).pack(side="top", pady=30)

        # q&a labels
        self.fc_prompt_label = tk.Label(
            frame, text="", font=self.deseret_font, bg="#EDE4BE"
        )
        self.fc_prompt_label.pack(side="top", pady=30)

        self.fc_answer_label = tk.Label(
            frame, text="", font=self.header_font_2, bg="#EDE4BE"
        )
        self.fc_answer_label.pack(side="top", pady=20)

        self.fc_name_label = tk.Label(
            frame, text="", font=self.header_font_3, bg="#EDE4BE"
        )
        self.fc_name_label.pack(pady=5)

        self.fc_pronunciation_label = tk.Label(
            frame, text="", font=self.main_text_font, bg="#EDE4BE", fg="#555555"
        )
        self.fc_pronunciation_label.pack(pady=5)

        self.show_answer_btn = tk.Button(
            frame,
            text="Flip",
            font=self.button_font_1,
            command=self.show_flashcard_answer,
            bg="#FFFFDB",
        )

        # difficulty selection buttons
        self.fc_grade_frame = tk.Frame(frame, bg="#EDE4BE")
        tk.Button(
            self.fc_grade_frame,
            text="Incorrect",
            command=lambda: self.grade_flashcard(1),
            font=self.main_text_font,
            bg="#ffcccc",
        ).pack(side="left", padx=5)
        tk.Button(
            self.fc_grade_frame,
            text="Hard",
            command=lambda: self.grade_flashcard(2),
            font=self.main_text_font,
            bg="#ffffcc",
        ).pack(side="left", padx=5)
        tk.Button(
            self.fc_grade_frame,
            text="Good",
            command=lambda: self.grade_flashcard(3),
            font=self.main_text_font,
            bg="#ccffcc",
        ).pack(side="left", padx=5)
        tk.Button(
            self.fc_grade_frame,
            text="Easy",
            command=lambda: self.grade_flashcard(4),
            font=self.main_text_font,
            bg="#ccddff",
        ).pack(side="left", padx=5)

        self.back_button = tk.Button(
            frame,
            text="Back - 𐐒𐐈𐐗",
            command=self.go_back,
            font=self.button_font_1,
            bg="#FFFFDB",
        ).pack(side="bottom", pady=15)

        self.show_frame(frame)

        # review session
        self.due_cards = get_due_cards(self.cards, self.current_day)
        self.current_card_index = 0
        self.load_next_flashcard()

    # decide which flashcard will be next
    def load_next_flashcard(self):
        self.fc_answer_label.config(text="")
        self.fc_name_label.config(text="")
        self.fc_pronunciation_label.config(text="")
        self.fc_grade_frame.pack_forget()

        if self.current_card_index < len(self.due_cards):
            card = self.due_cards[self.current_card_index]
            self.fc_prompt_label.config(text=card.prompt)
            self.show_answer_btn.pack(side="bottom", pady=50)
        else:
            self.fc_prompt_label.config(
                text="All done for this session! \n Restart the program if you want to \n continue from the beginning."
            )
            self.show_answer_btn.pack_forget()

    # flip the flashcard
    def show_flashcard_answer(self):
        if self.current_card_index < len(self.due_cards):
            card = self.due_cards[self.current_card_index]
            name = getattr(card, "name", "Unknown")
            pronunciation = getattr(card, "pronunciation", "Unknown")

            self.fc_answer_label.config(text=f"keyboard encoding: {card.answer}")
            self.fc_name_label.config(text=f"Deseret name: {name}")
            self.fc_pronunciation_label.config(text=f"Sounds like: {pronunciation}")

            self.show_answer_btn.pack_forget()
            self.fc_grade_frame.pack(pady=10)

    # add difficulty grading information to the card
    def grade_flashcard(self, quality):
        card = self.due_cards[self.current_card_index]
        update_card(card, quality)
        self.current_card_index += 1
        self.load_next_flashcard()
