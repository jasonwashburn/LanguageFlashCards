from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
SMALL_FONT = ("Arial", 40, "italic")
LARGE_FONT = ("Arial", 60, "bold")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.gif")
card_back_img = PhotoImage(file="images/card_back.gif")
canvas.create_image(400, 263, image=card_front_img)
small_text = canvas.create_text(400, 150, font=SMALL_FONT, text='small text')
large_text = canvas.create_text(400, 263, font=LARGE_FONT, text='large text')
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.gif")
wrong_button = Button(image=wrong_button_img, borderwidth=0, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="images/right.gif")
right_button = Button(image=right_button_img, borderwidth=0, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()
