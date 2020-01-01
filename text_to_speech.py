import tkinter as tk  # To create GUI
from gtts import gTTS  # Google Text To Speech
from playsound import playsound  # To play the audio

# Creating the UI window
ui_window = tk.Tk()
ui_window.title("Text To Speech")
ui_window.geometry("200x100")

label = tk.Label(ui_window, text="Enter the Text here:")
label.grid(row=0, column=0)

entry = tk.Entry(ui_window)
entry.grid(row=1, column=0)


def convert_to_speech():
    # Functionality to convert text to speech
    text = entry.get()
    speech = gTTS(text=text, lang="en")
    # Make sure audio folder is already present or else it will give error
    speech.save('./audio/test.mp3')
    playsound('./audio/test.mp3')


button = tk.Button(ui_window, text="Go", command=convert_to_speech)
button.grid(row=1, column=1)

# `mainloop()` is infinite loop used to run the application,
# wait for an event to occur and process the event till the window is not closed.
ui_window.mainloop()
