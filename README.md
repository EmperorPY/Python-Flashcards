# Python Basics Flash Cards

A desktop flash card app I made to help me revise Python basics while I was learning it.

## What it does

This is a local desktop app that shows you a Python question, lets you check the answer, and then moves on to a new random card. It has 113 cards across 10 categories, and you can pick a category from a dropdown to study just one topic at a time.

## Why I made this

I wanted a quick way to test myself on the Python basics I was learning and to help other people learn, and building the tool was good practice for working with JSON data and CustomTkinter.

## Features

* 113 flash cards covering Python basics, stored in a JSON file so new cards are easy to add.
* 10 categories: Core Types, Variables and Data Types, Input and Output, Operators, Strings, Lists and Tuples, Dictionaries, Control Flow, Functions, and Errors and General.
* Category dropdown that is built automatically from the JSON file, so a new category appears without changing any code.
* "Check" button to reveal the answer and "Next Card" button for a new random question.
* Modern dark-mode interface built with CustomTkinter.
* File paths handled with the Python OS module, so it runs from any folder.

## What I learned

* Didn't learn much but was good practice

## How to run

Make sure you install the required package first:
```bash
pip install customtkinter
```
Then download the script and `flashcards.json`, keep them in the same folder, and run the Python file:
```
python PythonBasicsFlashCards.py
```

## Made with

Python, CustomTkinter, json, random, os.

## Future improvements

* Don't repeat a card until every card in the category has been shown.
* A score counter for the cards I got right.
* A button to add my own cards from inside the app.
* More categories, like loops and file handling.
