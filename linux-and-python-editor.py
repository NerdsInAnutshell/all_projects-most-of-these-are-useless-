#linux and python editor
import os
option = input("which coding language do you want to use? (python3,linux)\n")
while True:
    if option == "python3":
        command = input(">>> ")
        with open("thg.py","a") as f:
            f.write(f"\n{command}")
            if command[-1] == ":":
                f.write("\n    pass")
        if command != "cls":
            os.system("python3 thg.py")
        else:
            os.system(command)
    elif option == "linux":
        command = input(">>> ")
        if command.split(">")[0] == "cat":
            with open(command.split(">")[1],"a") as f:
                while command.lower() != "exit":
                    command = input()
                    if command.lower() != "exit":
                        f.write(f"\n{command}")
        else:
            os.system(command)
#...Program finished with exit code 0
