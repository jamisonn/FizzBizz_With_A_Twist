import os
import tkinter
from tkinter import *
from playsound import playsound
'''
root = Tk()
frame = Frame(root)
frame.pack()
root.geometry("200x100")
'''
FizzSound = os.path.dirname(__file__) + '\\Sounds/Hi-Hat-Closed-Hit-A1-www.fesliyanstudios.com.mp3'
BuzzSound = os.path.dirname(__file__) + '\\Sounds/Bass-Drum-Hit-Level-5a-www.fesliyanstudios.com.mp3'
#Add a color GUI to change based on if fizz or buzz is selected

def FizzBuzzMethod(num):
    if num % 3 == 0:
        print("Fizz")
        playsound(FizzSound)
        #frame = tkinter.Frame(root, bg="blue")
        #frame.pack()

    if num % 5 == 0:
        print("Buzz")
        playsound(BuzzSound)
        #frame = tkinter.Frame(root, bg="red")
        #frame.pack()

    if num % 5 and num % 3 == 0:
        print("FizzBuzz")
        #frame = tkinter.Frame(root, bg="purple")
        #frame.pack()
        playsound(FizzSound)
        playsound(BuzzSound)



def FizzBuzzLoop():
    i = 1
    while i < 100:
        FizzBuzzMethod(i)
        i += 1

'''
Button = Button(root, text="text me", command=FizzBuzzLoop)
Button.pack()
root.mainloop()
'''