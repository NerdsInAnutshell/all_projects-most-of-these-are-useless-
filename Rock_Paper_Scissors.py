from tkinter import *
import random,os
os.system("cls")
root = Tk()
root.title("Rock, Paper, Scissors!")
compete = []
def get_fancy(string):
    fancy = "𝓪 𝓫 𝓬 𝓭 𝓮 𝓯 𝓰 𝓱 𝓲 𝓳 𝓴 𝓵 𝓶 𝓷 𝓸 𝓹 𝓺 𝓻 𝓼 𝓽 𝓾 𝓿 𝔀 𝔁 𝔂 𝔃 𝓐 𝓑 𝓒 𝓓 𝓔 𝓕 𝓖 𝓗 𝓘 𝓙 𝓚 𝓛 𝓜 𝓝 𝓞 𝓟 𝓠 𝓡 𝓢 𝓣 𝓤 𝓥 𝓦 𝓧 𝓨 𝓩".split(" ")
    alph = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
    fancytext = ""
    for i in string:
        if i != " ":
            fancytext+=fancy[alph.index(i)] if i.isalpha() == True else i
        else:
            fancytext+="  "
    return fancytext
vs = None
def add(thg):
    compete = []
    compete.append(thg)
    compete.append(["rock","paper","scissors"][random.randint(0,2)])
    winner = "Tie!"
    if compete[0] != compete[1]:
        if "rock" in compete and "scissors" in compete:
            winner = "Rock!"
        if "rock" in compete and "paper" in compete:
            winner = "Paper!"
        if "paper" in compete and "scissors" in compete:
            winner = "Scissors!"
    res = " vs ".join(compete) + "The winner is..." + winner
    vs=Label(root,text=get_fancy(f"""""") if winner != "Tie!" else "Tie!").pack()
rock,paper,scissors= Button(root, text="\U0001faa8 (rock)", command=lambda: add("rock")).pack(),Button(root, text="\U0001f4c4 (paper)", command=lambda:add("paper")).pack(),Button(root, text="\u2702\ufe0f (scissors)", command=lambda:add("scissors")).pack()
root.mainloop()
