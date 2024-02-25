import os

from playsound import playsound
FizzSound = os.path.dirname(__file__) + '\\Hi-Hat-Closed-Hit-A1-www.fesliyanstudios.com.mp30'
BuzzSound = os.path.dirname(__file__) + '\\Sounds/Bass-Drum-Hit-Level-5a-www.fesliyanstudios.com.mp3'


def FizzBuzzMethod(num):
    if num % 3 == 0:
        print("Fizz")
        playsound(FizzSound)
    if num % 5 == 0:
        print("Buzz")
        playsound(BuzzSound)
    if num % 5 and num % 3 == 0:
        print("FizzBuzz")
        playsound(FizzSound)
        playsound(BuzzSound)


i = 1
while i < 100:
    FizzBuzzMethod(i)
    i += 1
