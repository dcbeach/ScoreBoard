import tkinter as tk
from tkinter import *
from tkinter import ttk

scoreboardview = Tk()
scoreboardview.title("Score Board")
scoreboardview.geometry("1000x500+200+200")

player_frame = []
score_label = []
player_label = []
change_entry = []
scores = []
minus_button = []
plus_button = []
change_name_button = []

winning_score_label = Label(scoreboardview, text="Score needed to win: ", font=('Courier', 30))
winning_score_label.pack(side=TOP)
change_entry = Entry(scoreboardview, width=30)
change_entry.pack(side=TOP)


def set_score():
    global winScore
    scoreText = "Score needed to win: "
    newScore = change_entry.get()
    if change_entry.get().isdigit():
        winning_score_label.config(text=scoreText + str(newScore))
        winScore = int(newScore)


set_score_button = Button(scoreboardview, text="Set Score", command=set_score)
set_score_button.pack(side=TOP)


def check_for_winner(player_score, index):
    try:
        if player_score >= winScore:
            winning_score_label.config(text="We have a winner: " + player_label[index]['text'])
    except NameError:
        print("Set a win score!")


def increase_score(index):
    scores[index] += 1
    score_label[index].config(text=str(scores[index]))
    check_for_winner(scores[index], index)


def decrease_score(index):
    scores[index] -= 1
    score_label[index].config(text=str(scores[index]))
    check_for_winner(scores[index], index)


def change_name(index):
    newName = change_entry.get()
    if len(newName) <= 8:
        player_label[index].config(text=newName)


for i in range(5):
    scores.append(0)
    player_frame.append(Frame())
    player_label.append(Label(player_frame[i], text="Player", font=('Courier', 30)))
    score_label.append(Label(player_frame[i], text="0", font=('Courier', 44)))
    minus_button.append(Button(player_frame[i], text="-", command=(lambda x=i: decrease_score(x)), font=('Courier', 20)))
    plus_button.append(Button(player_frame[i], text="+", command=(lambda x=i: increase_score(x)), font=('Courier', 20)))
    change_name_button.append(Button(player_frame[i], text="Change Name", command=(lambda x=i: change_name(x))))
    change_name_button[i].pack(side=TOP)
    player_label[i].pack(side=TOP, expand=True, pady=20)
    score_label[i].pack(side=TOP, expand=True, pady=20)
    minus_button[i].pack(side=LEFT, padx=15)
    plus_button[i].pack(side=LEFT, padx=15)
    player_frame[i].pack(side=LEFT, expand=True)


scoreboardview.mainloop()
