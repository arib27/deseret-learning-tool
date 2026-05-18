# deseret learning tool - 𐐼𐐯𐑅𐑆𐐯𐑉𐐯𐐻 𐑊𐐲𐑉𐑌𐐮𐑍 𐐻𐐭𐑊

organization:

```
.
├── /config
|          
└── /data                   text, images, and resources 
|
├── /src                    primary functions
│   ├── /cards.py             flashcards
│   └── /gui.py               user interface
│   └── /typing_mode.py       typing practice
|
└── main.py                 run this to use the program 

```

### testing and use
Clone the repo in your terminal. Make sure to check requirements.txt for any libraries you need to install. From your command line, open the "deseret-learning-tool" folder, and run "main.py".
You can tell that the program is currently running as expected if:
1. A tkinter GUI opens onto a main page titled "Deseret Learning Tool", with an image loaded in the center
  and a few buttons.
2. The 'Begin' button opens a menu. The 'Program Instructions' button opens the instructions page. The 'Illinois Deseret Consortium' button opens the associated webpage in your default browser. The 'Quit' button closes the program.
3. The typing mode allows you to practice, fonts are loaded correctly, and you get feedback on your answers.
  The flashcards mode should display a character and allow you to check the answer and rate the difficulty.

### description
In this project I plan to create a learning application for the Deseret alphabet. The Deseret is a phonetic writing system used to write English, developed by the early Mormon community in the 1850s for purposes of orthographic reform and cultural differentiation. This application will be structured similar to other language-learning or flashcard applications, and will teach users to read and write in the Deseret alphabet using spaced repetition. Users will be able to gain access to the program through my research colloquium. This project will hopefully be used to train new research assistants working in the IDC, as well as be available for any interested public.