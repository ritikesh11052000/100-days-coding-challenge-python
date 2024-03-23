# word peech recognition code: -
import tkinter as tk
from tkinter import ttk
import random
import speech_recognition as sr

def evaluate_pronunciation(correct_word, user_word):
    if correct_word.lower() == user_word.lower():
        return True
    return False

score = 0

def on_microphone_button_click():
    global score
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        root.after(5000)
        audio = recognizer.listen(source)
    try:
        user_word = recognizer.recognize_google(audio)
        print("You said: " + user_word)
        feedback_label.config(text="You said: " + user_word)
        if evaluate_pronunciation(random_word, user_word):
            feedback_label.config(text=feedback_label.cget("text") + "\nCorrect pronunciation! You earned 1 point.")
            score += 1
            score_label.config(text="Score: {}".format(score))
        else:
            feedback_label.config(text=feedback_label.cget("text") + "\nIncorrect pronunciation. You lost 1 point.")
            score -= 1
            score_label.config(text="Score: {}".format(score))
    except sr.UnknownValueError:
        print("Could not understand audio")
        feedback_label.config(text="Could not understand audio")
    except sr.RequestError as e:
        print("Error fetching results: {0}".format(e))
        feedback_label.config(text="Error fetching results: {0}".format(e))

def on_random_word_button_click():
    global random_word
    words = ["apple", "banana", "orange", "grape", "pineapple"]
    random_word = random.choice(words)
    word_label.config(text="Word to pronounce: " + random_word)
    feedback_label.config(text="")

root = tk.Tk()
root.title("Word Pronouncer Game")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

word_label = ttk.Label(frame, text="Word to pronounce:", font=("Helvetica", 14))
word_label.grid(row=0, column=0, padx=(0, 10), pady=(10, 0))

random_word_button = ttk.Button(frame, text="Generate Random Word", command=on_random_word_button_click)
random_word_button.grid(row=1, column=0, padx=(0, 10), pady=(10, 0))

feedback_label = ttk.Label(frame, text="", font=("Helvetica", 12))
feedback_label.grid(row=2, column=0, padx=(0, 10), pady=(10, 0))

microphone_button = ttk.Button(frame, text="Speak", command=on_microphone_button_click)
microphone_button.grid(row=3, column=0, padx=(0, 10), pady=(10, 0))

score_label = ttk.Label(frame, text="Score: 0", font=("Helvetica", 12))
score_label.grid(row=4, column=0, padx=(0, 10), pady=(10, 0))

root.mainloop()



