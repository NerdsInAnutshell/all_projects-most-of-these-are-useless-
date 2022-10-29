import sys,tty,random
from time import time
penguin = "🐧➳"
cd = None
tty.setraw(sys.stdin.fileno())
x,y,bx,by = 1,0,random.randint(10,50),1
s=time()
def collision(cords1,cords2):
    return cords1[0] == cords2[0] and cords1[1] == cords2[1]
xmax = 134
ymax = 21
print("Press any key to start")
while True:
    key = sys.stdin.read(1)
    if key == "w":
        y-=1
    if key == "s":
        y+=1
    if key == "a":
        x-=1
    if key == "d":
        x+=1
    print("\033c",end="")
    cd = key
    if x<0 or x==0:
        x=1
    if x == xmax:
        y+=1
        x=1
    if y<0:
        y=0
    xpos,ypos = " "*x,"\n"*y
    print(f"{ypos}{xpos}{penguin}")
