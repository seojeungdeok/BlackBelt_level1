#!/usr/bin/python

from random import randint

no = randint(1,10)

while True:
    guess_no = int(input("Guess the number : "))
    if no==guess_no:
        print("Correct!")
        break
    else:
        print("Wrong, try again!")

