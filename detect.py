import pickle
import spam
from tkinter import *

with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)

def detect():
    user_input = input1.get()
    features = spam.create_features(user_input)
    answer.config(text=clf.classify(features))

root = Tk()
root.title('Spam detector')
root.geometry('400x300')
root.resizable(width=False, height=False)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label1 = Label(topFrame, text='Enter the word: ')
label1.pack()

input1 = Entry(topFrame)
input1.pack()

button1 = Button(topFrame, text='Detect', command=detect)
button1.pack()

button2 = Button(bottomFrame, text='Quit',fg='red', command=quit)
button2.pack()

answer = Label(topFrame, text='')
answer.pack()

root.mainloop()