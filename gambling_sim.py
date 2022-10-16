# investment simulation
import random
import pandas as pd
def investing(invstmnt,cycles):
    money = 0
    total = 0
    thg = invstmnt
    lst = []
    nums = []
    running = True
    for i in range(cycles):
        if running == True:
            luck = random.randint(1,2)
            if luck == 1:
                money+=thg+10
                thg+=10
            else:
                money = abs(money-thg)
            total+=money
            nums.append(money)
            lst.append(f"You now have {money} dollars")
    with open("investments.txt","a") as f:
            f.truncate(0)
            for i in lst:
                f.write(i+"\n")
    with open("investments.txt","r") as f:
        df = pd.read_csv("investments.txt",sep=" ")
    times = df.shape[0] + 1
    print(df)
    print(f"you invested {total} dollars, you also invested {times} times")
    print(f"the most money you had while investing was {max(nums)}")
investment,cycles=input().split(",")
investing(int(investment),int(cycles))
