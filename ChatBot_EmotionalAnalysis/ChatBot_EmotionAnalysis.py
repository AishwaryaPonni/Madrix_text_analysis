import tensorflow as tf
import numpy as np 
from keras.preprocessing.sequence import pad_sequences

# Loading the emotionAnalysis Model
new_model = tf.keras.models.load_model('E:/ChatBot/emotion_analyser_english')
import pickle

# Loading the pickled tokenizer
with open('E:/ChatBot/emotion_tokenizer', 'rb') as handle:
    tokenizer = pickle.load(handle)


def prediction(text):
  emotion = ['joy','sadness','anger','fear','love','surprise']
  # l = list(text)
  sequences = tokenizer.texts_to_sequences([text])
  test = pad_sequences(sequences)
  return emotion[np.around(new_model.predict(test), decimals=0).argmax(axis=1)[0]]


def chatBotResponse(text):
    sentiment = prediction(text);    
    if(sentiment=="joy"):
        print(sentiment)
        return "Be joyful!"
    elif sentiment =="sadness":
        print(sentiment)
        return "Don't be sad! Cheer up"
    elif sentiment =="anger":
        print(sentiment)
        return "Think with a calm mind"
    elif sentiment =="fear":
        print(sentiment)
        return "Seize your fears!"
    elif sentiment =="love":
        print(sentiment)
        return "Awwwww"
    elif sentiment =="surprise":
        print(sentiment)
        return "Oh that must've come as a shock!"
        
      

#Creating GUI with tkinter
import tkinter
from tkinter import *

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatBotResponse(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("SentimentAnalysis_ChatBot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial", padx=10, pady=10)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", padx= 32, pady=5,
                    bd=0, bg="#00ADB5", activebackground="#AAD8D3",fg='#eeeeee',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()