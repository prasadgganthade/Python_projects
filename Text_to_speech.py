import pyttsx3
from tkinter import *
import os

window = Tk()

window.geometry('450x300')
window.resizable(0,0)

window.title('Text to speech project')
window.configure(bg='AliceBlue')

# object
engine = pyttsx3.init()

# title label
Label(window,text='Text-to-speech',font='Aerial 20 bold',bg='AliceBlue',fg='blue2').pack()


# text box label and text box
msg = StringVar()
Label(window,text='Enter-text',font='Aerial 15 bold',bg='AliceBlue').place(x=40,y=60)
entry_field = Entry(window,textvariable=msg,width=60)
entry_field.place(x=40,y=100,height=25)

voices = engine.getProperty('voices')
_voice = True
# functions for converting text to speech
def toggle_voice():
    global  _voice
    if _voice:
        engine.setProperty('voice',voices[1].id) #female
        _voice = False
    else:
        engine.setProperty('voice',voices[0].id)
        _voice = True

def text_to_speech():

    message = entry_field.get()
    engine.say(message) # convert text to speech

    # engine.save_to_file(message,'t2s.mp3') #we can also save to audio
    engine.runAndWait() # plat the speech

    engine.stop()

def exit():
    window.destroy()

def reset():
    msg.set('')

# buttons
Button(window,text='Play',font='Aerial 15 bold',command=text_to_speech,bg='Blue').place(x=60,y=150)
Button(window,text='Reset',font='Aerial 15 bold',command=reset,bg='Blue').place(x=180,y=150)
Button(window,text='Exit',font='Aerial 15 bold',command=exit,bg='Blue').place(x=310,y=150)
Button(window,text='ChangeVoice',font='Aerial 15 bold',command=toggle_voice,bg='Blue').place(x=130,y=150)

window.mainloop()