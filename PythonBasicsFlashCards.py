# Import customtkinter, a modern version of tkinter with nicer-looking widgets
import customtkinter as ctk
# Import json so we can read the flashcards.json file
import json
# Import random so we can pick random cards
import random
# Import os so we can build the path to the JSON file
import os

# ---- Finding the JSON file ----
# __file__ is this script. abspath gives its full path and dirname gives the folder it is in.
# This means the JSON file is found even if the script is run from a different folder.
script_dir = os.path.dirname(os.path.abspath(__file__))

# Open flashcards.json (in the same folder as this script) for reading, using UTF-8 encoding
with open(os.path.join(script_dir, "flashcards.json"), "r", encoding="utf-8") as f:
    # json.load turns the file's text into a Python list of dictionaries
    # Each dictionary is one card with "category", "question" and "answer"
    cards = json.load(f)

# The card currently on screen. Starts as a random card from the whole deck.
card = random.choice(cards)


# ---- Functions ----

def next_card():
    """Pick a new random card from the chosen category and show its question."""
    # "global" lets us change the card variable that lives outside this function
    global card
    # Read what is currently selected in the dropdown
    chosen = category_list.get()
    # Start with an empty list that will hold the cards we are allowed to pick from
    pool = []
    # Go through every card in the deck
    for c in cards:
        # Keep the card if "All Categories" is selected, or if its category matches the dropdown
        if chosen == "All Categories" or c["category"] == chosen:
            # Add it to the pool
            pool.append(c)
    # Pick one random card from the pool and remember it as the current card
    card = random.choice(pool)
    # Replace the text on the card with the new card's question
    card_label.configure(text=card["question"])


def show_answer():
    """Show the answer for the card that is on screen right now."""
    # Replace the question text with the current card's answer
    card_label.configure(text=card["answer"])


# ---- Main window ----

# Create the main application window
root = ctk.CTk()
# Set the window size: 400 pixels wide, 600 tall
root.geometry("400x600")
# Use dark mode (dark background, light text)
ctk.set_appearance_mode("dark")
# Text shown in the window's title bar
root.title("Python Basics Flash Cards")

# ---- Title ----

# The heading label at the top of the window
title_label = ctk.CTkLabel(root, text="Python Basics Flash Cards", font=("Arial", 30))
# Show it in the window, with 10 pixels of space above and below
title_label.pack(pady=10)

# ---- Category dropdown ----

# Start the list of dropdown options with the "all" option first
categories = ["All Categories"]
# Go through every card
for c in cards:
    # Only add a category if it isn't already in the list, so each one appears once
    if c["category"] not in categories:
        categories.append(c["category"])

# Create the dropdown menu using the list above
# width=220 makes it wide enough for long names
# state="readonly" means you can only pick from the list, not type in it
# command runs next_card() whenever a new category is picked (the lambda receives the choice but ignores it)
category_list = ctk.CTkComboBox(root, values=categories, width=220, state="readonly", command=lambda choice: next_card())
# Show "All Categories" in the dropdown when the app starts
category_list.set("All Categories")
# Show the dropdown in the window
category_list.pack(pady=10)

# ---- The card ----

# A rounded, outlined frame that acts as the flashcard
# fg_color="transparent" means the inside has no colour of its own
card_frame = ctk.CTkFrame(root, width=300, height=400, corner_radius=45, border_width=2, border_color="gray", fg_color="transparent")
# Show the card in the window
card_frame.pack(pady=20)
# Stop the frame from shrinking to fit its contents, so it stays 300 x 400
card_frame.propagate(False)

# The label inside the card that shows the question (or answer)
# wraplength=250 makes long text wrap onto the next line instead of running off the card
card_label = ctk.CTkLabel(card_frame, text=card["question"], font=("Arial", 28), wraplength=250)
# The Check button: shows the answer when clicked
check_button = ctk.CTkButton(card_frame, text="Check", command=show_answer)
# The Next Card button: shows a new random question when clicked
next_button = ctk.CTkButton(card_frame, text="Next Card", command=next_card)

# The buttons are packed first, at the bottom, so they stay in place when the text changes
# Next Card goes first, so it ends up at the very bottom
next_button.pack(side="bottom", pady=10)
# Check goes above Next Card
check_button.pack(side="bottom", pady=5)
# The question text fills the space above the buttons
card_label.pack(pady=10)

# Start the app's main loop, which keeps the window open and listening for clicks
root.mainloop()