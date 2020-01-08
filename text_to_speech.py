import tkinter as tk  # To create GUI
import time  # Used for time stamp on audio file
from gtts import gTTS  # Google Text To Speech
from gtts import lang  # Languages available in gtts
from playsound import playsound  # To play the audio

# function to return key for any value 
def get_key(val):
    for key, value in languages.items():
        if val == value:
            return key

    return "Key doesn't exist"

def convert_to_speech():
    # Functionality to convert text to speech
    if not entry.get():
        # If nothing is entered in textbox then return
        return False
    text = entry.get()
    seleced_language = defaultSelect.get()

    lang = get_key(seleced_language) # For different accent audio
    speech = gTTS(text=text, lang=lang)

    time_stamp = time.strftime("%Y%m%d_%H%M%S")
    # Make sure audio folder is already present or else it will give error
    generate_file_name = f'./audio/audio_{lang}_{time_stamp}.mp3'

    speech.save(generate_file_name)
    playsound(generate_file_name)

# Creating the UI window
ui_window = tk.Tk()
ui_window.title("Text To Speech")
ui_window.geometry("200x100")

label = tk.Label(ui_window, text="Enter the Text here:")
label.grid(row=0, column=0)

entry = tk.Entry(ui_window)
entry.grid(row=1, column=0)

languages = lang.tts_langs()

defaultSelect = tk.StringVar(ui_window)
defaultSelect.set(languages['en'])
options = languages.values()
dropdown = tk.OptionMenu(ui_window, defaultSelect, *options)
dropdown.grid(row=2, column=0)

button = tk.Button(ui_window, text="Convert", command=convert_to_speech)
button.grid(row=1, column=1)

# `mainloop()` is infinite loop used to run the application,
# wait for an event to occur and process the event till the window is not closed.
ui_window.mainloop()
