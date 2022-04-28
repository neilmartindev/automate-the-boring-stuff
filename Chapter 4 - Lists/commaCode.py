from multiprocessing.connection import wait
from tkinter import N
from matplotlib.pyplot import pause
from numpy import insert

spam = ['apples', 'bananas', 'tofu', 'cats']

spam.insert(3, 'and')

print('Do you to add anything more to the list? y/n')
answer = input()

if answer == 'y':
    print('Append another value')
    newValue = input()
    spam.insert(2, newValue)
    print('New value added successfully')
    
elif answer == 'n':
    print('Exiting program...')
    print('Printing list...')
    exit

print(spam)
