# This is a bit of python to figure how well you did in a test
# It should ask for your score and how much it is out of then give you a grade
# Grades are numbered 1-9, 9 being the best.
# If it is too low it should say U

import time

# Getting the score
score = input("Enter your number of marks: ")
out_of = input("Enter the total possible marks: ")

# Converting to numbers
score = float(score)
out_of = float(out_of)
percentage = (score / out_of) * 100

def dramatic_pause(text1, text2, text3, text4):
    time.sleep(0.5)
    print(text1)
    time.sleep(0.5)
    print(text2)
    time.sleep(0.5)
    print(text3)
    time.sleep(1.5)
    print(text4)


print("You scored", percentage, "%")



dramatic_pause("Calculating grade...", "Please wait...", "Almost done...", "Here is your grade:")