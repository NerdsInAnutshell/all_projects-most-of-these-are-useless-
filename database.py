# account database
import hashlib as hl
import os
user,password = input().split(",")
option = input("sign in or log in?\n")
check = False
if option == "sign in":
  with open("accounts.txt","a") as f:
    with open("accounts.txt","r") as f:
        accounts = [i for i in f.readlines()]
    for i in accounts:
        if user == i.split(",")[0]:
          if check == False:
              print("Sorry, that username is taken")
              check = True
if check == False:
    f = open("accounts.txt","a")
    f.write(f"{user},{hl.sha256(password.encode()).hexdigest()}\n")
    f.close()
    print("account successfully created!")
elif option == "log in":
    with open("accounts.txt","r") as f:
        if os.path.getsize("accounts.txt") != 0:
               accounts = [i for i in f.readlines()]
        for i in accounts:
            if user == i.split(",")[0] and hl.sha256(password.encode()).hexdigest() == i.split(",")[1]:
                logged = "logged in"
                print(f"{logged} succesfully!")
        else:
          try:
            x = lambda x: print(logged)
          except:
              print("log in failed")
