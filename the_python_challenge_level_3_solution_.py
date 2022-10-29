import urllib.request as opener
nothing = "12345"
for i in range(400):
    with opener.urlopen(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}") as text:
        try:
            thg = list(str(text.read()).split(" ")[5])
            thg.remove(thg[-1])
            nothing = "".join(thg)
            print(nothing)
        except IndexError:
            print(text.read())
