import tkinter as tk
from gtts import gTTS
from playsound import playsound

# Creating the UI window
ui_window = tk.Tk()
ui_window.title("Text To Speech")
ui_window.geometry("200x100")

# Functionality


def conver_to_speech():
    text = entry.get()
    speech = gTTS(text=text, lang="en")
    speech.save(r'D:Project/Python/python-tts/audio/dummy.mp3')
    playsound(r'D:Project/Python/python-tts/audio/dummy.mp3')


label = tk.Label(ui_window, text="Enter the Text here:")
label.grid(row=0, column=0)

entry = tk.Entry(ui_window)
entry.grid(row=1, column=0)

button = tk.Button(ui_window, text="Go", command=conver_to_speech)
button.grid(row=1, column=1)

# `mainloop()` is infinite loop used to run the application,
# wait for an event to occur and process the event till the window is not closed.
ui_window.mainloop()
