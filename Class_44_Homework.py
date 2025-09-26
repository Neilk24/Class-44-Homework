from tkinter import *
import random
list = ['Rock', 'Paper', 'Scissors']
def decide_win(user, computer):
    if user == computer:
        return 'Tie!'
    elif (user == 'Rock' and computer == 'Scissors' ) or (user == 'Paper' and computer == 'Rock') or (user == 'Scissors' and computer == 'Paper'):
        return 'User!'
    else:
        return 'Computer!'
    
def play(user_choice):
    computer_choice = random.choice(list)
    result = decide_win(user_choice, computer_choice)
    user_label.config(text=f'You: {user_choice}')
    computer_label.config(text=f'Computer: {computer_choice}')
    if result == 'Tie!':
        result_label.config(text='Its a tie!', fg = 'black')
    elif result == 'User!':
        result_label.config(text='You win!', fg = 'Green')
    else:
        result_label.config(text='Computer wins!', fg = 'Red')
root = Tk()
root.geometry('400x400')
root.title('Length Converter App')
title = Label(root, text='Rock, Paper, Scissors')
title.pack(pady = 10)
frame = Frame(root)
frame.pack(pady = 10)
Button(frame, text="Rock", width = 12, command = lambda: play('Rock')).grid(row = 0, column = 0, padx = 5)
Button(frame, text="Paper", width = 12, command = lambda: play('Paper')).grid(row = 0, column = 1, padx = 5)
Button(frame, text="Scissors", width = 12, command = lambda: play('Scissors')).grid(row = 0, column = 2, padx = 5)
user_label = Label(root, text='You: ')
computer_label = Label(root, text='Computer: ')
user_label.pack()
computer_label.pack()
result_label = Label(root, text='Make your move! ')
result_label.pack(pady=10)
root.mainloop()