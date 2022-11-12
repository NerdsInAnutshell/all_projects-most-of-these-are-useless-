from tkinter import *
root = Tk()
thg = ""
root.title("Random Word Generator")
def generate(length):
    from random import choice as ch
    from random import randint as r
    try:
        thg.destroy()
    except:
        pass
    endings,vowels,consos,word = "ds,sh,rt,ce".split(","),[i for i in "aeiou"],[i for i in "bcdfghjklmnpqrstvwxyz"],""
    for i in range(1,length-2):
        if i%2==1:
            word+=ch(consos)
        else:
            word+=ch(vowels)
    word+=ch(vowels)+ch(endings)
    thg = Label(root,text=get_fancy(word))
    thg.pack()
def get_fancy(string):
    fancy = "𝓪 𝓫 𝓬 𝓭 𝓮 𝓯 𝓰 𝓱 𝓲 𝓳 𝓴 𝓵 𝓶 𝓷 𝓸 𝓹 𝓺 𝓻 𝓼 𝓽 𝓾 𝓿 𝔀 𝔁 𝔂 𝔃 𝓐 𝓑 𝓒 𝓓 𝓔 𝓕 𝓖 𝓗 𝓘 𝓙 𝓚 𝓛 𝓜 𝓝 𝓞 𝓟 𝓠 𝓡 𝓢 𝓣 𝓤 𝓥 𝓦 𝓧 𝓨 𝓩".split(" ")
    alph = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
    fancytext = ""
    for i in string:
        fancytext+=fancy[alph.index(i)]
    return fancytext
gen = Button(root, text=get_fancy("Generate"), command=lambda:generate(int(float(intro.get().strip()))), bg="green")
intro = Entry(root,bg="blue",width=23)
intro.insert(0,"Length of random word...")
gen.pack()
intro.pack()
root.mainloop()
