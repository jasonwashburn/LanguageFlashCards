from tkinter import *
import pandas as pd
import random
from pandas import errors

BACKGROUND_COLOR = "#B1DDC6"
SMALL_FONT = ("Arial", 40, "italic")
LARGE_FONT = ("Arial", 60, "bold")
new_word = {}
# ---------------------------- READ DATA ------------------------------- #
try:
    data_df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data_df = pd.read_csv("data/french_words.csv")
except pd.errors.EmptyDataError:
    data_df = pd.read_csv("data/french_words.csv")
finally:
    data_dict = data_df.to_dict(orient="records")


# ---------------------------- FLASHCARD LOGIC ------------------------------- #
def new_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_img, image=card_front_img)
    if len(data_dict) != 0:
        new_word = random.choice(data_dict)
        canvas.itemconfig(title, fill='black', text='French')
        canvas.itemconfig(word, fill='black', text=new_word.get('French'))
        flip_timer = window.after(3000, flip_card)
    else:
        canvas.itemconfig(title, fill='black', text='Congratulations!')
        canvas.itemconfig(word, fill='black', text='All Cards Complete')


def flip_card():
    global new_word
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title, fill='white', text='English')
    canvas.itemconfig(word, fill='white', text=new_word.get('English'))


def got_right():
    global new_word
    if len(data_dict) != 0:
        data_dict.remove(new_word)
        new_df = pd.DataFrame(data_dict)
        new_df.to_csv('words_to_learn.csv', index=False)
        window.title(f"Flash Cards: {len(data_dict)} cards remaining.")
        new_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(f"Flash Cards: {len(data_dict)} cards remaining.")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.gif")
card_back_img = PhotoImage(file="images/card_back.gif")
card_img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, font=SMALL_FONT, text='French')
word = canvas.create_text(400, 263, font=LARGE_FONT, text='Word')
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.gif")
wrong_button = Button(image=wrong_button_img, command=new_card, borderwidth=0, highlightbackground=BACKGROUND_COLOR,
                      highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="images/right.gif")
right_button = Button(image=right_button_img, command=got_right, borderwidth=0, highlightbackground=BACKGROUND_COLOR,
                      highlightthickness=0)
right_button.grid(column=1, row=1)

# ---------------------------- MAIN PROGRAM ------------------------------- #
flip_timer = window.after(3000, flip_card)
new_card()
window.mainloop()
