from tkinter import *
import pandas as pd
import random
from pandas import errors

BACKGROUND_COLOR = "#B1DDC6"
SMALL_FONT = ("Arial", 40, "italic")
LARGE_FONT = ("Arial", 60, "bold")
new_word = {}
# ---------------------------- READ DATA ------------------------------- #
# Reads saved progress list from 'words_to_learn.csv' if it exists and isn't empty,
# otherwise loads a new list from 'data/french_words.csv'

try:
    data_df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data_df = pd.read_csv("data/french_words.csv")
except pd.errors.EmptyDataError:
    data_df = pd.read_csv("data/french_words.csv")
finally:
    data_list = data_df.to_dict(orient="records")


# ---------------------------- FLASHCARD LOGIC ------------------------------- #

def new_card():
    # Pulls a new word from the list of remaining words, updates the card and starts the flip timer
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_img, image=card_front_img)
    if len(data_list) != 0:  # Only try to pull a new word if the list is not empty
        new_word = random.choice(data_list)
        canvas.itemconfig(title, fill='black', text='French')
        canvas.itemconfig(word, fill='black', text=new_word.get('French'))
        flip_timer = window.after(3000, flip_card)
    else:
        # If no words remain in list, congratulate user.
        canvas.itemconfig(title, fill='black', text='Congratulations!')
        canvas.itemconfig(word, fill='black', text='All Cards Complete')


def flip_card():
    # Flips card over to reveal translated word.
    global new_word
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title, fill='white', text='English')
    canvas.itemconfig(word, fill='white', text=new_word.get('English'))


def got_right():
    # If user got it right, remove card from the list and update the save file 'words_to_learn.csv'
    global new_word
    if len(data_list) != 0:
        data_list.remove(new_word)
        new_df = pd.DataFrame(data_list)
        new_df.to_csv('words_to_learn.csv', index=False)
        window.title(f"Flash Cards: {len(data_list)} cards remaining.")  # Update window title to reflect progress
        new_card()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title(f"Flash Cards: {len(data_list)} cards remaining.")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas (card images, and text)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.gif")
card_back_img = PhotoImage(file="images/card_back.gif")
card_img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, font=SMALL_FONT, text='French')
word = canvas.create_text(400, 263, font=LARGE_FONT, text='Word')
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button_img = PhotoImage(file="images/wrong.gif")
wrong_button = Button(image=wrong_button_img, command=new_card, borderwidth=0, highlightbackground=BACKGROUND_COLOR,
                      highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_button_img = PhotoImage(file="images/right.gif")
right_button = Button(image=right_button_img, command=got_right, borderwidth=0, highlightbackground=BACKGROUND_COLOR,
                      highlightthickness=0)
right_button.grid(column=1, row=1)

# ---------------------------- MAIN PROGRAM ------------------------------- #
flip_timer = window.after(3000, flip_card)  # Start the flip timer
new_card()  # Display the first card
window.mainloop()
