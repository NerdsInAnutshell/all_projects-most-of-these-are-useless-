def decode(string):
    thg=string
    decoded=""
    for i in thg:
        if i == "y":
            decoded+="a"
        elif i == "z":
            decoded+="b"
        else:
            if i.isalpha() == True:
                decoded+=chr(ord(i)+2)
            else:
                decoded+=i
    print(decoded)
decode("map")
